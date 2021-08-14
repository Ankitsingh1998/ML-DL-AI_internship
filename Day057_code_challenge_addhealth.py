#Day057 - code challenge addhealth (adolescence health)
import pandas as pd
df = pd.read_csv('addhealth.csv')

df.isnull().any(axis=0)
# Removing NaN values with Most Frequent value of the column
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])

#Problem 1:
features_treg = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',  
           'DEP1','ESTEEM1']].values
labels_treg = df["TREG1"].values

from sklearn.model_selection import train_test_split
features_train1, features_test1, labels_train1, labels_test1 = train_test_split(features_treg, labels_treg, test_size=0.3, random_state=1)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
lgr1 = LogisticRegression(max_iter=200)
lgr1.fit(features_train1, labels_train1)

prediction_lgr1 = lgr1.predict(features_test1)   

#KNN
from sklearn.neighbors import KNeighborsClassifier
kn1 = KNeighborsClassifier()
kn1.fit(features_train1, labels_train1)

prediction_kn1 = kn1.predict(features_test1)

from sklearn.metrics import confusion_matrix
lgr1_cm = confusion_matrix(labels_test1, prediction_lgr1)
lgr1_score = lgr1.score(features_test1, labels_test1)

kn1_cm = confusion_matrix(labels_test1, prediction_kn1)
kn1_score = kn1.score(features_test1, labels_test1)

print ("model accuracy using confusion matrix (LogisticRegression): "+str(lgr1_cm))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(lgr1_score*100,2))+'%')

print ("model accuracy using confusion matrix (KNN): "+str(kn1_cm))
print ("model accuracy using .score() function (KNN): "+str(round(kn1_score*100,2))+'%')

#Problem 2:
features_expel = df[["BIO_SEX","VIOL1"]].values
labels_expel = df["EXPEL1"].values

from sklearn.model_selection import train_test_split
features_train2, features_test2, labels_train2, labels_test2 = train_test_split(features_expel, labels_expel, test_size=0.3, random_state=2)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
lgr2 = LogisticRegression(max_iter=200)
lgr2.fit(features_train2, labels_train2)

prediction_lgr2 = lgr2.predict(features_test2)   

#KNN
from sklearn.neighbors import KNeighborsClassifier
kn2 = KNeighborsClassifier()
kn2.fit(features_train2, labels_train2)

prediction_kn2 = kn2.predict(features_test2)

from sklearn.metrics import confusion_matrix
lgr2_cm = confusion_matrix(labels_test2, prediction_lgr2)
lgr2_score = lgr2.score(features_test2, labels_test2)

kn2_cm = confusion_matrix(labels_test2, prediction_kn2)
kn2_score = kn2.score(features_test2, labels_test2)

print ("model accuracy using confusion matrix (LogisticRegression): "+str(lgr2_cm))
print ("model accuracy using .score() function (LogisticRegression): "+str(round(lgr2_score*100,2))+'%')

print ("model accuracy using confusion matrix (KNN): "+str(kn2_cm))
print ("model accuracy using .score() function (KNN): "+str(round(kn2_score*100,2))+'%')

