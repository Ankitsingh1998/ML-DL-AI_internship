#Day089 - code challenge deliveryfleet

"""
file = deliveryfleet.csv

Here we need Two driver features: mean distance driven per day 
(Distance_feature) and the mean percentage of time a driver was >5 mph over 
the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.

Perform K-means clustering again to further distinguish speeding drivers from 
those who follow speed limits, in addition to the rural vs. urban division.

Label accordingly for the 4 groups.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('deliveryfleet.csv') #Dataframe - DataSet
features = df.iloc[:, [1, 2]].values


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
WCSS = []
for i in range(1, 11):
    kmeans_model = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans_model.fit(features)
    WCSS.append(kmeans_model.inertia_) #WCSS values corresponding to different clusters
plt.plot(range(1, 11), WCSS)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


#Fitting K-Means cluster to the dataset
kmeans_model = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
y_kmeans = kmeans_model.fit_predict(features)

#Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 20, c = 'red', label = 'Rural Drivers')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 20, c = 'cyan', label = 'Urban Drivers')
plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1], s = 40, c = 'black', label = 'Centroids')
plt.title('Clusters of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()


#Fitting K-Means to the dataset (for Rash and Safe Drivers)
kmeans_model2 = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
y_kmeans = kmeans_model2.fit_predict(features)

#Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 20, c = 'red', label = 'Rural Safe Drivers')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 20, c = 'blue', label = 'Urban Safe Drivers')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 20, c = 'yellow', label = 'Urban Rash Drivers')
plt.scatter(features[y_kmeans == 3, 0], features[y_kmeans == 3, 1], s = 20, c = 'cyan', label = 'Rural Rash Drivers')
plt.scatter(kmeans_model2.cluster_centers_[:, 0], kmeans_model2.cluster_centers_[:, 1], s = 40, c = 'black', label = 'Centroids')
plt.title('Clusters of Drivers')
plt.xlabel('Distance Feature')
plt.ylabel('Speeding Feature')
plt.legend()
plt.show()
