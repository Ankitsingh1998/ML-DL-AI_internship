#Day043, Day044 - KNN Classification
"""
caesarian column meanings:
Delivery number : {1,2,3,4}
Delivery time : {0:timely, 1:premature ,2:latecomer}
Blood Pressure : {0:low, 1:normal, 2:high}
Heart Problem : {0:apt, 1:inept}  #apt-normal, inept-there is heart problem
caesarian : {0:No, 1:Yes}
"""
#22,1,0,1,0
import pandas as pd
df = pd.read_csv('caesarian.csv')

df.shape
df.isnull().any(axis=0)
df.columns.tolist()
df.dtypes

#features, labels
features = df.iloc[:,0:5].values
labels = df.iloc[:,5].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3)

#build the model - classifier
#KNN - KNeighboursClassifier
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
#n_neighbours is k
#p = 2 means euclidian's distance and p = 1 means manhattan distance

classifier.fit(features_train,labels_train)

prediction = classifier.predict(features_test)

model_comparison = pd.DataFrame(zip(prediction, labels_test))

from sklearn.metrics import confusion_matrix
comparison = confusion_matrix(labels_test, prediction)
#confusion matrix is here only for classifier
accuracy = (comparison[0][0] + comparison[1][1])/comparison.sum()

import numpy as np
female_x = [22, 1, 0, 1, 0]
female_x = np.array(female_x)
female_x = female_x.reshape(1, 5)
classifier.predict(female_x)

classifier.score(features_test, labels_test)
