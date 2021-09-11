#Day089 - code challenge tshirts

"""
T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium, 
and large. How would you figure out the actual size of these 3 types of shirt 
to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of 
the data as stated above.

file_name = "tshirts.py"
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tshirts.csv')

features = df.iloc[:,[1,2]].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
WCSS = []
for i in range(1, 11):
    kmeans_model = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans_model.fit(features)
    WCSS.append(kmeans_model.inertia_)
plt.plot(range(1, 11), WCSS)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
#n_clusters = 3 is best suited as it has maximum angle in WCSS vs number of clusters graph

#With n_clusters = 3, higher angle in WCSS vs number of clusters graph
kmeans_model = KMeans(n_clusters = 3, init = 'k-means++', random_state = 1)
y_kmeans = kmeans_model.fit_predict(features)

#Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 20, c = 'cyan', label = 'Medium')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 20, c = 'red', label = 'Large')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 20, c = 'blue', label = 'Small')
plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1], s = 40, c = 'black', label = 'Centroids')
plt.title('3 Clusters of T-Shirts')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.legend()
plt.show()

#With n_clusters = 2, smaller angle in WCSS vs number of clusters graph
kmeans_model = KMeans(n_clusters = 2, init = 'k-means++', random_state = 2)
y_kmeans = kmeans_model.fit_predict(features)

#Visualising the clusters
plt.scatter(features[y_kmeans == 0, 0], features[y_kmeans == 0, 1], s = 20, c = 'cyan', label = 'Medium')
plt.scatter(features[y_kmeans == 1, 0], features[y_kmeans == 1, 1], s = 20, c = 'red', label = 'Large')
plt.scatter(features[y_kmeans == 2, 0], features[y_kmeans == 2, 1], s = 20, c = 'blue', label = 'Small')
plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1], s = 40, c = 'black', label = 'Centroids')
plt.title('2 Clusters of T-Shirts')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.legend()
plt.show()
