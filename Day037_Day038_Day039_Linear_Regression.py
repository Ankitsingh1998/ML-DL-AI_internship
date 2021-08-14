#Day037, Day038, Day039 - categorical data to numeric representation
import pandas as pd
df = pd.read_csv('Salary_Classification.csv')

df.shape
df.columns.tolist()
df.isnull().any(axis=0)
df.dtypes

#features and labels:

features = df.iloc[:,0:4].values
labels = df.iloc[:,-1].values

#department columns
#we need to convert categorical data to numeric representation
#encode our categorical data in numeric
#onehotencoding

#info -> encoded (Morse code) -> transmission -> decode -> info
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

C_Transformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')

import numpy as np
features = np.array(C_Transformer.fit_transform(features), dtype = np.float32)
#dummy variables created to create new columns which were not earlier(0, 1 & 2)
#0 - Development column, 1 - Testing column & 2 - UX column

features = features[:,1:] #to remove redundant/dependent variable we removed 1st column

#train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

#feature scaling/normalization - 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
#training data - 70%
#fit --> mean, std
#transform --> formula

features_test = sc.transform(features_test)
#testing data  30%
#fit_transform, fit - mean, std from this 20% data only
#transform - mean, std from train data

from sklearn.linear_model import LinearRegression
regression = LinearRegression() #create an object

regression.fit(features_train, labels_train)

predicted = regression.predict(features_test)

pd.DataFrame(zip(predicted, labels_test))

predicted_train = regression.predict(features_train)

pd.DataFrame(zip(predicted_train, labels_train))

#regression.score(features_test, predicted) - will give one only ??
#score - accuracy
train_accuracy = regression.score(features_train, labels_train)
test_accuracy = regression.score(features_test, labels_test)

print('Our model trained accuracy is: '+str(train_accuracy*100)+'%')
print('Our model tested accuracy is: '+str(test_accuracy*100)+'%')

#Now, predicting for new features:
regression.fit(features, labels)
x = [['Development', 1100, 2, 3], ['UX', 2500, 3, 4.6], ['Testing', 1800, 2, 1.2]]
x = np.array(x)
x = np.array(C_Transformer.transform(x), dtype = np.float32)
x = x[:,1:]
#transform
regression.predict(x)

#Taking input to predict
y = [[str(input('Enter your Department among these three:\nDevelopment\nTesting\nUX: \n')), int(input('Enter your total work done in hours: ')), int(input('Enter number of certifications done by you: ')), float(input('Enter your years of experience: '))]]
y = np.array(y)
y = np.array(C_Transformer.transform(y), dtype = np.float32)
y = y[:,1:]
regression.predict(y)

55389.836, 69826.97 , 36603.527