#Day092 - PCA (forward selection dimension reduction method)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Wine.csv')

df.shape
df.columns.to_list()

features = df.iloc[:,0:13].values
labels = df.iloc[:,13].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=0)

from sklearn.preprocessing import StandardScaler #Features scaling
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


#PCA: forward elimination
from sklearn.decomposition import PCA
pca = PCA(n_components=3)

features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)

features_train.shape
features_test.shape

#How much is the loss and how much information we are able to retain
explained_variance = pca.explained_variance_ratio_
print(explained_variance)
#First paramater (PC1) is holding 37.32% of the 13D data/total data
#Second parameter (PC2) is holding 18.81% of the 13D data/total data
#Third parameter (PC3) is holding 10.89% of the 13D data/total data
total = explained_variance.sum()
print(total*100) #Total data holding


#Fitting LogisticRegression to our nw datset
from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(random_state=0)

lgr.fit(features_train,labels_train)

#Prediction
predictions = lgr.predict(features_test)
print(list(zip(predictions, labels_test)))

#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, predictions)

score = (cm[0][0]+cm[1][1]+cm[2][2])/cm.sum()
print('score of our model is:',score*100,'%')


"""
#Visualising the test set results
x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1
z_min, z_max = features_train[:, 2].min() - 1, features_train[:, 2].max() + 1

xx, yy, zz = np.meshgrid(np.arange(x_min, x_max, 0.01),np.arange(y_min, y_max, 0.01), np.arange(z_min, z_max, 0.01))
#Obtain labels for each point in mesh using the model.
#ravel() is equivalent to flatten method.
#data dimension must match training data dimension, hence using ravel
Z = lgr.predict(np.c_[xx.ravel(), yy.ravel(), zz.ravel()]).reshape(xx.shape)

#Plot the points, we have three labels (1,2,3)
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], features_test[labels_test == 1, 2], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 2, 0], features_test[labels_test == 2, 1], features_test[labels_test == 2, 2], 'go', label='Class 2')
plt.plot(features_test[labels_test == 3, 0], features_test[labels_test == 3, 1], features_test[labels_test == 3, 2], 'bo', label='Class 3')

#plot the decision boundary
plt.contourf(xx, yy, zz, Z, alpha=.5)
plt.show()

print(cm)
"""

#Dump components relations with features:
df_features = pd.DataFrame(features)
df_pca =  pd.DataFrame(pca.components_,columns=df_features.columns,index = ['PC-1','PC-2','PC-3'])
print(df_pca)
