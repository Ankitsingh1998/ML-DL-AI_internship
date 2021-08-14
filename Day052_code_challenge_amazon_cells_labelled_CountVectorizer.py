#Day052 - code challenge amazon cells labelled
import pandas as pd
df = pd.read_table('amazon_cells_labelled.txt', sep='\t', names=['review', 'liked'])
#by default, sep='\t', need not be mentioned.
#features = review column, labels = liked column

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

corpus = []
for i in range(1000):
    review = re.sub(r'[^a-zA-Z]', ' ', df['review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    
    review = ' '.join(review)
    
    corpus.append(review)

print(corpus)
print(len(corpus))

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)

#It is known as sparse matrix of the features nD array
features = cv.fit_transform(corpus).toarray() #1500 columns
labels = df.iloc[:,-1].values

print(features.shape)
print(labels.shape)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

#Using KNN model (Method 1):
from sklearn.neighbors import KNeighborsClassifier
knm = KNeighborsClassifier()
knm.fit(features_train, labels_train)

labels_prediction_knm = knm.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_knm = confusion_matrix(labels_test, labels_prediction_knm)
kn_score = (cm_knm[0][0]+cm_knm[1][1])/cm_knm.sum()

print('Accuracy of the KNN model is: '+str(kn_score.round(4)))
#for better NLP we need more data

#Using Navie Baye's (Method 2):
from sklearn.naive_bayes import GaussianNB
gnm = GaussianNB()
gnm.fit(features_train, labels_train)

labels_prediction_gnm = gnm.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_gnm = confusion_matrix(labels_test, labels_prediction_gnm)
gn_score = (cm_gnm[0][0]+cm_gnm[1][1])/cm_gnm.sum()

print('Accuracy of the Naive Baye\'s model is: '+str(gn_score.round(4)))

#Using Logistic Regression (Method 3):
from sklearn.linear_model import LogisticRegression
lrm = LogisticRegression()
lrm.fit(features_train, labels_train)

labels_prediction_lrm = lrm.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_lrm = confusion_matrix(labels_test, labels_prediction_lrm)
lm_score = (cm_lrm[0][0]+cm_lrm[1][1])/cm_lrm.sum()

print('Accuracy of the Logistic Regression model is: '+str(lm_score.round(4)))
