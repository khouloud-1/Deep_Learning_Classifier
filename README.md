Deep Learning for Hierarchical Arabic Text Classification


Djelloul BOUCHIHA1, Abdelghani BOUZIANE2, Noureddine DOUMI3, Farouk Omar BERBOUCHI4, Aymen Abdelghani KIBIR5, Nihad MEBARKI6 and Badia Achouak BENAMER7

If you use a software from this page, please cite us as follows:
Djelloul BOUCHIHA, Abdelghani BOUZIANE, Noureddine DOUMI, Farouk Omar BERBOUCHI, Aymen Abdelghani KIBIR, Nihad MEBARKI and Badia Achouak BENAMER. Deep Learning for Hierarchical Arabic Text Classification. Submitted (still under review).

If you need help, contact Djelloul BOUCHIHA: 
bouchiha@cuniv-naama.dz; bouchiha.dj@gmail.com; djelloul.bouchiha@univ-sba.dz; 

Before using any software from this page, please follow carefully the following notes:

First you have to download the WiHArD dataset from https://data.mendeley.com/datasets/kdkryh5rs2/2. Download the whole dataset as one CSV file (WiHArD.csv)

Note that the deep learning classifier has been implemented using the Scientific Python Development Environment (Spyder IDE, version 4.1.5):
 

Before running the classifier, you have to install some additional Python packages: 
Since we are using Anaconda environment including Spyder (Python editor), then we add packages through Anaconda Prompt terminal:
 

For the first time, check the already installed packages with:
C:\...>pip list


For BERT embedding, you have to install:
For Arabic language:
C:\...>pip install -U tensorflow
C:\...>pip install -U transformers
Look at (https://pytorch.org/get-started/locally/) to install pytorch
C:\...>conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch



Next, you will find the Python classifier source code:
ARBERT-NN_Functional_Global.py


Next are some error and warning messages that you may meet when dealing with our classifier:


When launching the Arabic BERT model, if you get the following error message:
RuntimeError: The size of tensor a (532) must match the size of tensor b (512) at non-singleton dimension 1

So, you must reduce the string length introduced to the BERT model. For example: Arabic_Bert_Model_T(i[0:2000])



If you receive the following error message:
ValueError: The first argument to `Layer.call` must always be passed.

This means that the BERT model must be launched before building the Neural Network model.


