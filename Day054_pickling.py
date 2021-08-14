#Day054 - pickling
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

#Tf-idf : Term frequency - inverse document frequency
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(min_df=5).fit(features_train)
#min_df means ignore the terms/words that appears less than the set value, by default it is 5. 

features_train_vectorized = vect.transform(features_train)

#Model building
#statsquest yt channel - Logistic Regression
from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(max_iter = 10000)
lgr.fit(features_train_vectorized, labels_train)

predictions = lgr.predict(vect.transform(features_test))

from sklearn.metrics import confusion_matrix
lgr_cm_score = confusion_matrix(labels_test, predictions)

from sklearn.metrics import roc_auc_score
lgr_roc_score = roc_auc_score(labels_test, predictions)

#save as pickle -will run on my machine
import pickle
file = open('pickle_lgr_model.pkl', 'wb')
pickle.dump(lgr, file) #to save our model in the pickle file

#pickle the vocabulary
pickle.dump(vect.vocabulary_, open('features.pkl', 'wb'))



