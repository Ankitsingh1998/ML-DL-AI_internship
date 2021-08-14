#Day047 - code challenge mushrooms
import pandas as pd

df= pd.read_csv('mushrooms.csv')
df.columns.tolist()

features = df[['odor', 'population', 'habitat']].values
labels = df[['class']].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer

La_en = LabelEncoder()
labels = La_en.fit_transform(labels) #0 --> edible, 1 --> poisioned

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder='passthrough')
features = cTransformer.fit_transform(features).toarray()

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state = 1)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5, p=2)
knn.fit(features_train, labels_train)
test_data_prediction = knn.predict(features_test)

from sklearn.metrics import confusion_matrix
con_mat = confusion_matrix(labels_test, test_data_prediction)

print ("Model Score for our KNN model is: "+str(round(knn.score(features_test,labels_test),4)*100)+"%")
