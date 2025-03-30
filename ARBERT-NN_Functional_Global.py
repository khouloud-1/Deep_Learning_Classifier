# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 12:30:04 2025

@author: Bouchiha
"""

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.utils.class_weight import compute_class_weight
from transformers import BertTokenizer, BertModel
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.regularizers import l2

# Load dataset
df = pd.read_csv("WiHArD.csv", encoding='utf-8')

# Define hierarchical category mapping
def map_categories(x):
    # Level 1 mapping (3 classes)
    if x in [1, 2, 3, 4]:
        level_1 = 0  # Culture
    elif x in [5, 6, 7, 8]:
        level_1 = 1  # History
    else:
        level_1 = 2  # Math
    
    # Level 2 mapping (9 classes)
    level_2_mapping = {
        1: 0, 2: 1, 3: 2, 4: 3, 
        5: 4, 6: 5, 7: 6, 8: 7, 
        9: 8, 10: 8, 11: 8, 12: 8
    }
    level_2 = level_2_mapping[x]
    
    return level_1, level_2

# Apply mappings
df['level_1'], df['level_2'] = zip(*df['category_code'].map(map_categories))

# Verify we have exactly 9 classes in level_2
unique_classes = np.unique(df['level_2'])
print("Unique level_2 classes:", unique_classes)
assert len(unique_classes) == 9, f"Level 2 should have exactly 9 classes, found {len(unique_classes)}"

# Split dataset
X_train, X_test, y_train_l1, y_test_l1, y_train_l2, y_test_l2 = train_test_split(
    df['text'], df['level_1'], df['level_2'], 
    test_size=0.3, 
    stratify=df[['level_1', 'level_2']],
    random_state=42
)

# Load ARBERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("UBC-NLP/ARBERT")
Bmodel = BertModel.from_pretrained("UBC-NLP/ARBERT")

# Improved BERT embeddings extraction
def Arabic_Bert_Model_G(texts):
    embeddings = []
    for text in texts:
        inputs = tokenizer(text, truncation=True, max_length=512, 
                         return_tensors="pt", padding='max_length')
        outputs = Bmodel(**inputs)
        # Use mean pooling of last hidden states
        last_hidden = outputs.last_hidden_state.detach().numpy()
        mean_pooled = np.mean(last_hidden, axis=1)[0]
        embeddings.append(mean_pooled)
    return np.array(embeddings, dtype=np.float32)

# Convert text to embeddings
print("Converting training texts to embeddings...")
X_train_emb = Arabic_Bert_Model_G(X_train)
print("Converting test texts to embeddings...")
X_test_emb = Arabic_Bert_Model_G(X_test)

# Compute class weights for Level 2
print("Computing class weights...")
class_weights = compute_class_weight('balanced', classes=unique_classes, y=y_train_l2)
class_weight_dict = {i: weight for i, weight in enumerate(class_weights)}
print("Class weights:", class_weight_dict)

# Build ANN model
print("Building model...")
input_layer = tf.keras.layers.Input(shape=(X_train_emb.shape[1],))
hidden_layer = tf.keras.layers.Dense(768, activation='relu', 
                                   kernel_regularizer=l2(0.01))(input_layer)
hidden_layer = tf.keras.layers.BatchNormalization()(hidden_layer)
hidden_layer = tf.keras.layers.Dropout(0.3)(hidden_layer)

# Level 1 output (3 classes)
level_1_output = tf.keras.layers.Dense(3, activation='softmax', 
                                     name="level_1_output")(hidden_layer)

# Level 2 output (9 classes)
level_2_hidden = tf.keras.layers.Dense(512, activation='relu', 
                                     kernel_regularizer=l2(0.01))(hidden_layer)
level_2_hidden = tf.keras.layers.BatchNormalization()(level_2_hidden)
level_2_hidden = tf.keras.layers.Dropout(0.3)(level_2_hidden)
level_2_output = tf.keras.layers.Dense(9, activation='softmax', 
                                     name="level_2_output")(level_2_hidden)

model = tf.keras.Model(inputs=input_layer, outputs=[level_1_output, level_2_output])

# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss={
        'level_1_output': 'sparse_categorical_crossentropy',
        'level_2_output': 'sparse_categorical_crossentropy'
    },
    loss_weights={
        'level_1_output': 0.3,
        'level_2_output': 0.7
    },
    metrics=['accuracy']
)

# Callbacks
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6)
]

# Create sample weights for level_2
sample_weights = np.array([class_weight_dict[cls] for cls in y_train_l2])

# Train model
print("Training model...")
history = model.fit(
    X_train_emb,
    {
        'level_1_output': y_train_l1,
        'level_2_output': y_train_l2
    },
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    sample_weight={'level_2_output': sample_weights},  # Using sample_weight instead of class_weight
    callbacks=callbacks,
    verbose=1
)

# Evaluate
print("Evaluating model...")
y_pred_l1, y_pred_l2 = model.predict(X_test_emb)
y_pred_l1 = np.argmax(y_pred_l1, axis=-1)
y_pred_l2 = np.argmax(y_pred_l2, axis=-1)

# Hierarchical metrics
def hierarchical_metrics(y_true_l1, y_true_l2, y_pred_l1, y_pred_l2):
    correct = np.logical_and(y_true_l1 == y_pred_l1, y_true_l2 == y_pred_l2)
    precision = np.sum(correct) / len(y_pred_l2)
    recall = np.sum(correct) / len(y_true_l2)
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1

h_precision, h_recall, h_f1 = hierarchical_metrics(y_test_l1, y_test_l2, y_pred_l1, y_pred_l2)

# Print results
print("\n=== Hierarchical Metrics ===")
print(f"Hierarchical Precision: {h_precision:.4f}")
print(f"Hierarchical Recall: {h_recall:.4f}")
print(f"Hierarchical F1-Score: {h_f1:.4f}")

#print("\n=== Level 1 Classification Report ===")
#print(classification_report(y_test_l1, y_pred_l1, target_names=['Culture', 'History', 'Math']))

#print("\n=== Level 2 Classification Report ===")
#print(classification_report(y_test_l2, y_pred_l2))
