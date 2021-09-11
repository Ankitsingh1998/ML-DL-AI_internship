#Day090 - DBSCAN (Unsupervised Machine Learning)
#DBSCAN - Density based and not centroid based

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

#Generate sample data
center_list = [[0, 1], [-1, -1], [1, -1]]

#make_blobs generates random points from any point from a list
features, labels = make_blobs(n_samples=750, centers = center_list, cluster_std=0.4, random_state=1)
#By default, two features are given by make_blobs

#print(features)
#print(labels)

#scattering all of these data points in matplotlib
plt.scatter(features[:,0], features[:,1], c='blue')
plt.show()


features = StandardScaler().fit_transform(features)

#scattering all the standardized data points in matplotlib
plt.scatter(features[:,0], features[:,1], c='red')
plt.show()

#DBSCAN
db_model = DBSCAN(eps=0.3, min_samples = 10).fit(features)

#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True

labels_predict = db_model.labels_ #belongs to which cluster id/number
print(labels_predict) #-1 --> means those datapoints belongs to no clusters

len(features[labels_predict==0])
len(features[labels_predict==1])
len(features[labels_predict==2])
len(features[labels_predict==-1])

#plotting in graph
plt.scatter(features[labels_predict==0, 0], features[labels_predict==0, 1], c='cyan', label='cluster1', marker='+')
plt.scatter(features[labels_predict==1, 0], features[labels_predict==1, 1], c='red', label='cluster2', marker='o')
plt.scatter(features[labels_predict==2, 0], features[labels_predict==2, 1], c='green', label='cluster3', marker='v')
plt.scatter(features[labels_predict==-1, 0], features[labels_predict==-1, 1], c='black', label='noise/no_cluster', marker='*')
plt.show()

#Performance of the dbscan


#Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_predict, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_predict, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_predict, labels))
print("Adjusted Rand Index: %0.3f"% metrics.adjusted_rand_score(labels_predict, labels))
print("Adjusted Mutual Information: %0.3f"% metrics.adjusted_mutual_info_score(labels_predict, labels))
print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(features, labels))


#Remmbering how to read data from datasets

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset iris dataset 
from sklearn.datasets import load_iris
iris = load_iris()

dataset = iris.data
