#Day049 - NLP
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

#reviewText --> features
#positivity --> label
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

#final vectorization transformation to numeric
features_train_vectorized = vect.transform(features_train)
#It's length will be --> row equal to row of features_train and column equal to vocabulary count
features_train.shape
len(feature_names)
features_train_vectorized.shape

