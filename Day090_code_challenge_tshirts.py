#Day090 - code challenge tshirts

"""
Create a program that fulfills the following specifications:
file = tshirts.csv

T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. 
How would you figure out the actual size of these 3 types of shirt to better 
fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of 
the data as stated above.
"""

import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt

df = pd.read_csv('tshirts.csv')

df.columns.to_list()
df.head()

features = df.iloc[:,[1,2]].values

#visualizing the plot
plt.scatter(features[:,0], features[:,1], c='blue')
plt.show()

#DBSCAN
from sklearn.cluster import DBSCAN

db_model = DBSCAN(eps=5, min_samples=3)
model = db_model.fit(features)

labels = model.labels_


#plotting teh clusters
plt.scatter(features[labels == 0, 0], features[labels == 0, 1],c='red', marker='+' ,label='Cluster1')
plt.scatter(features[labels == 1, 0], features[labels == 1, 1],c='cyan', marker='*' , label='Cluster2')
plt.scatter(features[labels == -1, 0],features[labels == -1, 1],c='black', marker='o', label='noise/no_cluster')
plt.legend()
plt.show()


print('Silhouette score for DBSCAN:',metrics.silhouette_score(features,labels))

#Observations on these clusters
data1 = features[labels==0]
data2 = features[labels==1]
data3 = features[labels==-1]

print('Cluster1 datapoints are:\n',data1)
print('Cluster2 datapoints are:\n',data2)
print('Noise/no_clusters in the dataset is:\n',data3)

print('Range of height for cluster1 is:',features[labels==0, 0].min(),'-',features[labels==0, 0].max(),'inches respectively.')
print('Range of weight for cluster1 is:',features[labels==0, 1].min(),'-',features[labels==0, 1].max(),'pounds respectively.')
print('Range of height for cluster2 is:',features[labels==1, 0].min(),'-',features[labels==1, 0].max(),'inches respectively.')
print('Range of weight for cluster2 is:',features[labels==1, 1].min(),'-',features[labels==1, 1].max(),'pounds respectively.')
print('Range of height for Noise/no_cluster is:',features[labels==-1, 0].min(),'-',features[labels==-1, 0].max(),'inches respectively.')
print('Range of weight for Noise/no_cluster is:',features[labels==-1, 1].min(),'-',features[labels==-1, 1].max(),'pounds respectively.')
