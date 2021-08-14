#Day033 - linear regression model testing
import pandas as pd
df = pd.read_csv('student_scores.csv')

"""
features = df['Hours'].values #values added to give data in a list and to remove index

labels = df['Scores'].values

from sklearn.linear_model import LinearRegression

#create an object
regression = LinearRegression()

features = features.reshape(25,1)
labels = labels.reshape(25,1)

regression.fit(features, labels)

regression.predict([[9.5]])

regression.predict(features)
"""

#To check whether our prdiction is nearest to accurate or not:
#by splitting data in two set - tran test split
#1. train set - used for training the model (60-80%)
#2. test model - to evaluate how good or bad our model is. (40-20%)

features = df['Hours'].values

labels = df['Scores'].values

##perfrom train-test split here
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
features_train = features_train.reshape(20,1)
regression.fit(features_train, labels_train)

features_test = features_test.reshape(5,1)
predicted = regression.predict(features_test)

list(zip(predicted, labels_test))

pd.DataFrame(zip(predicted, labels_test))

#score - accuracy (How much accurate our mpodel is??)
#train score
regression.score(features_train, labels_train)
"""
score uses this:
    First, predict(features_train)
    then, compare with labels_train
"""
#test score
regression.score(features_test, labels_test)

#train_test_split method: requires sequence of a data
#data can be a list, an ndarray, ora dataframe
list1 = [1,2,3,4,5,6,7,8,9,10,11]
import numpy as np
array = np.arange(11)
train, test = train_test_split(list1, test_size = 0.2, random_state = 0) #train_size=0.8 #each time random splitting of data

#train, test = train_test_split(list1, test_size = 0.2, random_state = 1)
#for each particular random_state, train and test datasets becomes constant.
#random_state can only be an integer
