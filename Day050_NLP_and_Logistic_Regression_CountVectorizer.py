#Day050 - NLP and Logistic Regression
import pandas as pd
df = pd.read_csv('Balanced_reviews.csv')

df.isnull().any(axis=0)
df.dropna(inplace=True)
df.shape

df = df[df['overall'] != 3]
df.shape
df['overall'].value_counts()

import numpy as np
df['positivity'] = np.where(df['overall'] > 3, 1, 0)
df.shape

df['positivity'].value_counts()

features = df['reviewText']
labels = df['positivity']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer().fit(features_train)

#To get the different words extracted from vocabulary
feature_names = vect.get_feature_names()
print(len(feature_names)) #length of the vocabulary
print(feature_names[9540:9550]) #check for some words

features_train_vectorized = vect.transform(features_train) #will transform and converts vocabulary into column with their counts for different rows

#features_train_vectorized.toarray()
#features_train_vectorized.todense()

#create the classifier(first model)
#SVM(Support vector machine)/SVC(Support vector classifier), KNN, Naive Bayes, Logistic Regression, Decision Trees, Random Forest
#Logistic Regression - binary classifier, works good for text data like NLP

from sklearn.linear_model import LogisticRegression
Log_rgr = LogisticRegression(dual=False, max_iter=10000, solver='lbfgs')

Log_rgr.fit(features_train_vectorized, labels_train)

prediction = Log_rgr.predict(vect.transform(features_test)) #prediction rows equal to rows of features_test

from sklearn.metrics import confusion_matrix

score_data = confusion_matrix(labels_test, prediction)

from sklearn.metrics import roc_auc_score
roc_auc_score(labels_test, prediction) #score of the model Method 1
(score_data[0][0]+score_data[1][1])/(score_data.sum()) #score Method 2

"""
59234+59467
Out[36]: 118701

_/131835
Out[37]: 0.9003754693366708

_ --> stores the last calculation and we can perform other calculations on it
in the next line in console.
"""

