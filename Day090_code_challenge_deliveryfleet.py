#Day090 - code challenge deliveryfleet

"""
Create a program that fulfills the following specifications:
file = deliveryfleet.csv

Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) 
and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers 
from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.
"""

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("deliveryfleet.csv")

df.isnull().any(axis=0)

df.info()

df.columns.to_list()

df.head()

features = df.iloc[:,[1,2]].values

#plotting the data in matplotlib
plt.scatter(features[:,0], features[:,1], c='b')
plt.show()

standardscaler = StandardScaler().fit(df)

df = standardscaler.transform(df)

#DBSCAN
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.30, min_samples=10).fit(df)

labels = db.labels_ 

#len(features[labels== 0])
#len(features[labels== 1])
#len(features[labels== 2])
#len(features[labels== -1])

#plotting the clusters in a scatterplot
plt.scatter(features[labels == 0 ,0], features[labels == 0, 1], c='cyan', marker='+', label='Cluster1')
plt.scatter(features[labels == 1, 0], features[labels == 1, 1], c='red', marker='*', label='Cluster2')
plt.scatter(features[labels == 2, 0], features[labels == 2, 1], c='yellow', marker='s', label='Cluster3')
plt.scatter(features[labels == 3, 0], features[labels == 3, 1], c='green', marker='s', label='Cluster4')
plt.scatter(features[labels == -1, 0], features[labels == -1, 1], c='black', marker='o', label='noise/no_cluster')
plt.title('Clusters of Drivers')
plt.xlabel('Distance_Feature')
plt.ylabel('Speeding_Feature')
plt.legend()
plt.show()