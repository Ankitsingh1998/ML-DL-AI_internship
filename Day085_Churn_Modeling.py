#Day085 - Churn Modeling
"""
Churn Modeling:
The customer churn, also known as customer attrition, refers to the phenomenon whereby
a customer leaves a service provider.

It is advantageous for banks to know what leads a client towards the decision to leave
the company.

Churn prevention allows companies to develop loyalty programs and retention campaigns 
to keep as many customers as possible.

In this code challenge, we use customer data from a bank to construct a predictive model
using deep learning for the likely churn customers.
"""

#ANN:

import pandas as pd
df = pd.read_csv('Churn_Modelling.csv') #to read the csv file
df.columns.to_list() #to display column names into list

df.shape #shape of the dataset

df['Geography'].head() #first 5 values in this column
df['Geography'].unique() #unique values in the region/country column

import numpy as np 
import matplotlib.pyplot as plt

features = df.iloc[:,3:13].values #without values it will be another dataset, with values it gets converted to numpy module
labels = df.iloc[:,13].values

#df.dtypes
#features[0:10,:]

#OneHotEncoder to convert geography and gender to numeric representation
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

column_transformer = ColumnTransformer([('encoder', OneHotEncoder(), [1,2])], remainder = 'passthrough')
#([(what we are performing, which encoder, columns)], remainder='passthrough' --> means rest columns gets unaffected)

features = np.array(column_transformer.fit_transform(features), dtype=np.float32)

features[0:10,:] #1st and 4th are dummy variables --> 1 to 3 column for Geography and 4 to 5 for Gender

#Handling dummy variables
features = features[:,1:] #for geography - handling dummy variables
features[0]

features = features[:,[0,1,3,4,5,6,7,8,9,10,11]] #for gender column - handling dummy variables
features[0]

features.shape

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

features_train[0]
features_test[0]

#keras libraries and packages for model training
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

#Adding the first hidden layer and input layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

#Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

#Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

#Now, compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(features_train, labels_train, batch_size = 10, epochs = 10)
#change number of epochs to change the score/accuracy

prediction = classifier.predict_classes(features_test)

#print(prediction)

len(prediction)

list(zip(labels_test, prediction))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, prediction)

score = (cm[0][0] + cm[1][1])/cm.sum()

print(score)
