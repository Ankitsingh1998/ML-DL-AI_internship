#Day093 - code challenge banknotes
"""
Suppose you are the manager of a bank and you have the problem of 
discriminating between genuine and counterfeit banknotes. You are measuring 
several distances on the banknote and the width and height of it.

Measuring these values of about 100 genuine and 100 counterfeit banknotes, 
Use the data set to set up a logical regression and is capable of 
discriminating between genuine and counterfeit money classification. 
(Import banknotes.csv)

(this data set contains data on Swiss francs currency; it has been obtained 
courtesy of H. Riedwyl )

Check the accuracy of your model using confusion matrix.

Then use k-fold cross validation to find actual mean accuracy of your model.

file_name - "banknotes.py"
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('banknotes.csv')
features = df.iloc[:, 1:-1].values
labels = df.iloc[:, -1].values

#Train Test Split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size = 0.3, random_state = 0)

#LogisticRegression
from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(random_state = 0)
lgr.fit(features_train, labels_train)

#Predictions
predictions_lgr = lgr.predict(features_test)
list(zip(predictions_lgr, labels_test))

#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(labels_test, predictions_lgr)
print(cm1)

score = (cm1[0][0]+cm1[1][1])/cm1.sum()
print('score is:',round(score*100,2))

#k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
k_fold_scores = cross_val_score(estimator = lgr, X = features_train, y = labels_train, cv = 10)
print ("Mean accuracy is : "+str(round(k_fold_scores.mean()*100,2))+"%")
print ("standard deviation : "+str(k_fold_scores.std()))

#xgboost
from xgboost import XGBClassifier
xgb = XGBClassifier()
xgb.fit(features_train, labels_train)

#Predictions
predictions_xgb = xgb.predict(features_test)
list(zip(predictions_xgb, labels_test))

#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(labels_test, predictions_xgb)
print(cm2)

score = (cm2[0][0]+cm2[1][1])/cm2.sum()
print('score is:',round(score*100,2))

#k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
k_fold_scores = cross_val_score(estimator = xgb, X = features_train, y = labels_train, cv = 10)
print ("Mean accuracy is : "+str(round(k_fold_scores.mean()*100,2))+"%")
print ("standard deviation : "+str(k_fold_scores.std()))
