#Day055 - nltk
import pandas as pd
df = pd.read_csv('Balanced_reviews.csv')

df.isnull().any(axis=0)
df.dropna(inplace=True)
df = df[df['overall'] != 3]

import numpy as np
df['positivity'] = np.where(df['overall'] > 3, 1, 0)

#NLP
#reviewText - cleanup perform - nltk
import nltk
import re
#nltk.download('stopwords') - to download or update the stopwords

from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords

cleaned_review = []
for i in range(0, df['reviewText'].count()):
    review = re.sub('[^a-zA-Z]', ' ', df.iloc[i,1])
    review = review.lower()
    review = review.split()

#now remove the stopwords
    review = [word for word in review if not word in stopwords.words('english')]

#stemming - similar words will get represented in one unique word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]

    review = ' '.join(review)
    cleaned_review.append(review)

#features - cleaned_review
#labels - df.iloc[:,-1]
from sklearn.feature_extraction.text import CountVectorizer
features_vectorized = CountVectorizer().fit_transform(cleaned_review)

labels = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features_vectorized, labels, test_size=0.3, random_state=42)

from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(max_iter=100000)

lgr.fit(features_train, labels_train)

labels_predicted = lgr.predict(features_test)

lgr.score(features_test, labels_test)
