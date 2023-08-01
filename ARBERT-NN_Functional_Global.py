# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:27:03 2022

@author: BOUCHIHA
"""

import tensorflow as tf

# Import the dataset (Dataset is taken from kaggle)
import pandas as pd

df = pd.read_csv("WiHArD.csv", encoding='utf-8')


df['tpc']=df['category_code'].apply(lambda x: 0 if x==1 else (1 if x==2 else (2 if x==3 else (3 if x==4 else (4 if x==5 else (5 if x==6 else (6 if x==7 else (7 if x==8 else (8 if x==9 else (9 if x==10 else (10 if x==11 else 11)))))))))))

# Split it into training and test data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['tpc'], test_size=0.3, train_size=0.7, stratify=df['tpc'])


# Arabic BERT Model
from transformers import BertTokenizer, BertModel
import torch

# ARBERT
BRT = "ARBERT"
tokenizer = BertTokenizer.from_pretrained("UBC-NLP/ARBERT")
Bmodel = BertModel.from_pretrained("UBC-NLP/ARBERT")

# Bert Model
def Arabic_Bert_Model_T(t_input):
    try:
        inputs = tokenizer(t_input, truncation=True, max_length = 512, return_tensors="pt")
        outputs = Bmodel(**inputs)
        print("Good input")
        return outputs.pooler_output.detach().numpy()[0]
    except:
        inputs = tokenizer("", return_tensors="pt")
        outputs = Bmodel(**inputs)
        print("Bad input")
        return outputs.pooler_output.detach().numpy()[0]       

def Arabic_Bert_Model_G(ts_input):
    A = list()
    for i in ts_input:
            A.append(Arabic_Bert_Model_T(i))    
    return tf.convert_to_tensor(A, dtype=tf.float32)


X_tr = Arabic_Bert_Model_G(X_train)
X_ts = Arabic_Bert_Model_G(X_test)


# Neural network layers
input_l = tf.keras.layers.Input(shape=(X_tr.shape[1],))
hidden_l = tf.keras.layers.Dense(768, activation='sigmoid', name="hidden_l")(input_l)
output_l = tf.keras.layers.Dense(12, activation='sigmoid', name="output_l")(hidden_l)

# Use inputs and outputs to construct a final model
NNmodel = tf.keras.Model(inputs=input_l, outputs = output_l)


NNmodel.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Train the model (Training phase)
NNmodel.fit(X_tr, y_train, epochs=100)



# Evaluate the model (Test phase)
from sklearn.metrics import classification_report
import numpy as np

y_predicted = NNmodel.predict(X_ts)
y_predicted = np.argmax(y_predicted, axis=-1)

print("\n\n----------------  Evaluation:  "+ BRT + "  -----------------------------------------------")
print(classification_report(y_test, y_predicted, zero_division=0))



# Inference (Prediction phase)
print("\n\n\----------------  Prediction  -----------------------------------------------")

x = 'هذا التراث الثقافي غير المادي المتوارث جيلا عن جيل، تبدعه الجماعات والمجموعات من جديد بصورة مستمرة، بما يتفق مع بيئتها وتفاعلاتها مع الطبيعة وتاريخها، وهو ينمي لديها الإحساس بهويتها والشعور باستمراريتها، ويعزز من ثم احترام التنوع الثقافي والقدرة الإبداعية البشرية.'#input('Enter your the text to be classified: ')
msg = [x]
X_pr = Arabic_Bert_Model_G(msg)


r = NNmodel.predict(X_pr)

# display the main category of the new text
main_topic_of_x = np.argmax(r[0])
print("\nMain class of the new text : ")
if (main_topic_of_x == 0): print('1- ثقافة')
elif  (main_topic_of_x == 1): print('2- ملابس')
elif  (main_topic_of_x == 2): print('3- طعام و شراب')
elif  (main_topic_of_x == 3): print('4- سياحة')
elif  (main_topic_of_x == 4): print('5- تاريخ')
elif  (main_topic_of_x == 5): print('6- أحداث')
elif  (main_topic_of_x == 6): print('7- إختراعات')
elif  (main_topic_of_x == 7): print('8- آثار')
elif  (main_topic_of_x == 8): print('9- رياضيات')
elif  (main_topic_of_x == 9): print('10- جبر')
elif  (main_topic_of_x == 10): print('11- تحليل')
elif  (main_topic_of_x == 11): print('12- هندسة')

# display all categories of the new text
r = r.flatten()
r = np.where(r > 0.8, 1, 0)
topics_of_x = np.flatnonzero(r == np.max(r))

print("\nAll classes of the new text : ")
for i in range(len(topics_of_x)):
    if (topics_of_x[i] == 0): print('1- ثقافة')
    elif  (topics_of_x[i] == 1): print('2- ملابس')
    elif  (topics_of_x[i] == 2): print('3- طعام و شراب')
    elif  (topics_of_x[i] == 3): print('4- سياحة')
    elif  (topics_of_x[i] == 4): print('5- تاريخ')
    elif  (topics_of_x[i] == 5): print('6- أحداث')
    elif  (topics_of_x[i] == 6): print('7- إختراعات')
    elif  (topics_of_x[i] == 7): print('8- آثار')
    elif  (topics_of_x[i] == 8): print('9- رياضيات')
    elif  (topics_of_x[i] == 9): print('10- جبر')
    elif  (topics_of_x[i] == 10): print('11- تحليل')
    elif  (topics_of_x[i] == 11): print('12- هندسة')
