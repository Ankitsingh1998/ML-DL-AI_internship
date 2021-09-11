#Day089 - WCSS and Silhouette Method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('xclara.csv')

features = df.iloc[:,[0,1]].values

from sklearn.cluster import KMeans

#WCSS Method: To determine optimla number of clusters
WCSS = []
for i in range(1,11):
    kmeans_model = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans_model.fit(features) #fit is used insteda od fit_predict --> only fitting no predictions
    #print("Cluster " + str(i) +  "  =  " + str(kmeans_model.inertia_))
    WCSS.append(kmeans_model.inertia_)

#print(WCSS)

#WCSS plotting
plt.plot(range(1,11), WCSS)
plt.title('Elbow Method') #Elbow method - optimal number of cluster where graph makes elbow shape. Here, n_clusters = 3
plt.xlabel('Numebr of clusters')
plt.ylabel("WCSS")
plt.show()
"""
Now, plot it and try to find Elbow, The elbow points is the right number of cluster.
Another way to detect the optimal number of cluster is Silhouette method.
Run the Silhouette Code, when the Silhouette score is maximum, 
it is the optimal number of clusters .
There is another way to find the right number of clusters
Known as Silhouette score.
Run the Silhouette Code, when the Silhouette score is maximum, it is the optimal 
number of clusters .
We need at least 2 clusters to Silhouette calculate score.
"""
"""
For two elbow, compare it with angle made by it. The Elbow with maximum angle
will give the optimal number of clusters.
"""

#Silhouette Score: Calculation to find optimal number of clusters
"""
The Silhouette Coefficient is defined for each sample and is composed of two scores:

a: The mean distance between a sample and all other points in the same class.
b: The mean distance between a sample and all other points in the next nearest cluster.
The Silhouette Coefficient s for a single sample is then given as:

score, s = (b - a)/max(a, b)
"""

from sklearn.metrics import silhouette_score

scores = []
for i in range(2, 11):
    kmeans_model = KMeans(n_clusters=i)
    predictions = kmeans_model.fit_predict(features)
    centers = kmeans_model.cluster_centers_

    score = silhouette_score(features, predictions, metric='euclidean')
    print("For n_clusters =",i,',',"The average silhouette_score is:", score)
    scores.append(score)

a = scores.index(max(scores))
n = a+2
print('Optimal number of clusters for this dataset is:',n)

