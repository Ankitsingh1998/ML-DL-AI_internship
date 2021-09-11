#Day089 - kMeans (Unsupervised Machine Learning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('xclara.csv')

df.shape #shape of dataframe
df.columns.to_list() #column_names into list
df.ndim #dimension of dataframe
df.isnull().any(axis=0) #axis = 0 for row wise null value checking

#type(df) #dataframe type is pandas.core.frame.DataFrame

features = df.iloc[:,[0,1]].values #values - to convert dataframe into numpy array

#type(features)

x = features[:,0]
y = features[:,1]

plt.scatter(x, y)
plt.show()

#K-means clustering: 3 clusters
from sklearn.cluster import KMeans #dir(sklearn.cluster)
#3 clustering is given because we already visualized it
kmeans_model = KMeans(n_clusters=3, init = 'k-means++', random_state=42)
predict_cluster = kmeans_model.fit_predict(features) #features passed only - Unsupervised ML

print(predict_cluster)

#Visualizing the clusters seperately
#plt.scatter(features[:,0][y_kmeans==0], features[:,1][y_kmeans==0])
plt.scatter(features[predict_cluster == 0, 0], features[predict_cluster == 0, 1], c='cyan', label='Cluster1')
plt.scatter(features[predict_cluster == 1, 0], features[predict_cluster == 1, 1], c='red', label='Cluster2')
plt.scatter(features[predict_cluster == 2, 0], features[predict_cluster == 2, 1], c='yellow', label='Cluster3')
plt.show()


"""
Centroid of the clusters:

Explain the concept of Center of Mass = Centroid 

                     Sum of x coordinates 
x of centroid   =   -----------------------
                    Total number of values 
                    

                     Sum of y coordinates 
y of centroid   =   -----------------------
                    Total number of values                     
"""

print(kmeans_model.cluster_centers_)  #coordinates of all centroids

print(kmeans_model.cluster_centers_[:, 0]) #x-coordinate of all centroids
print(kmeans_model.cluster_centers_[:, 1]) #y-coordinate of all centroids 

#Visualizing the clusters seperately with their centroids
plt.scatter(features[predict_cluster == 0, 0], features[predict_cluster == 0, 1], c='cyan', label='Cluster1')
plt.scatter(features[predict_cluster == 1, 0], features[predict_cluster == 1, 1], c='red', label='Cluster2')
plt.scatter(features[predict_cluster == 2, 0], features[predict_cluster == 2, 1], c='yellow', label='Cluster3')
plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1], c = 'black', label = 'Centroids')
plt.title('Clusters of datapoints alongwith their centroids')
plt.xlabel('X-Cordindates')
plt.ylabel('Y-Cordinates')
plt.legend()
plt.show()
