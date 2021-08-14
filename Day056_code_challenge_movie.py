#Day056 - code challenge movie
import pandas as  pd

df = pd.read_csv('movie.csv')

import re
import nltk

from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords

cleaned_text = []
for i in range(0, df['text'].count()):
    review = re.sub('[^a-zA-Z]', ' ', df.iloc[i,1])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in stopwords.words('english')]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    cleaned_text.append(review)

from sklearn.feature_extraction.text import CountVectorizer
features_vectorized = CountVectorizer().fit_transform(cleaned_text)

labels = df.iloc[:,0]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features_vectorized, labels, test_size=0.3, random_state=0)

from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(max_iter=200)

lgr.fit(features_train, labels_train)

labels_predicted = lgr.predict(features_test)

lgr.score(features_test, labels_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(labels_predicted, labels_test)

score = accuracy_score(labels_predicted, labels_test)

print('CountVector for Linear Regression performance on the dataset is: ' + str(cm))

print('Score for our model is: ' + str(score))