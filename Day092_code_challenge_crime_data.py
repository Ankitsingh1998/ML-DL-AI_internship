#Day092 - code challenge crime data
"""
Q1. Import Crime.csv File.
    Perform dimension reduction and group the cities using k-means based on 
    Rape, Murder and assault predictors.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('crime_data.csv')

df.shape
df.columns.to_list()

features = df.iloc[:, [1,2,4]].values #Murder, assault, rape

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)

#PCA: forward elimination
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

features = pca.fit_transform(features)

explained_variance = pca.explained_variance_ratio_ #loss
print(explained_variance)

print(explained_variance.sum())

#Elbow mathod
from sklearn.cluster import KMeans

WCSS = []
for i in range(1, 11):
    kmeans_model = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans_model.fit(features)
    WCSS.append(kmeans_model.inertia_)
    
print(WCSS)

#WCSS vs number of clusters        
plt.plot(range(1, 11), WCSS)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show() #4 clusters are best for this dataset

from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)

cluster_prediction = kmeans_model.fit_predict(features)

print(cluster_prediction)

#Add predicted column
df["pred_cluster"] = cluster_prediction

plt.scatter(features[:,0], features[:,1], color='red')
