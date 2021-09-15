#Day092 - code challenge iris
"""
Q2.The iris data set consists of 50 samples from each of three species of Iris 
flower (Iris setosa, Iris virginica and Iris versicolor).
Four features were measured from each sample: the length and the width 
of the sepals and petals, in centimetres (iris.data).
Import the iris dataset already in sklearn module using the following command
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets

iris = datasets.load_iris()

iris.keys() #dataset info
iris.DESCR #description of the dataset
iris.data  #features
iris.data.shape
iris.feature_names
iris.target 

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()
#df.to_csv('iris.csv')

features = df.iloc[:,0:].values #no labels - clustering

#PCA: forward elimination
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

features = pca.fit_transform(features)

explained_variance = pca.explained_variance_ratio_
print(explained_variance)

#Elbow mathod
from sklearn.cluster import KMeans

WCSS = []
for i in range(1, 11):
    kmeans_model = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans_model.fit(features)
    WCSS.append(kmeans_model.inertia_)
print(WCSS)

#Now plot wcss vs number of clusters   
plt.plot(range(1, 11), WCSS)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show() #3 clusters is best for this dataset as can be seen from the plot

from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)

cluster_prediction = kmeans_model.fit_predict(features)

print(cluster_prediction)

df["pred_cluster"] = cluster_prediction

df["pred_cluster"].value_counts(dropna=False)

#visualise
plt.scatter(features[:,0],features[:,1])