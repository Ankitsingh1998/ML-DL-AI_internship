#Day031 & Day032 - linear regression
import pandas as pd
df = pd.read_csv('student_scores.csv')

df.columns
df.columns.tolist() #for list conversion
df.shape

df.isnull().any(axis=0)

features = df['Hours'].values #values added to give data in a list and to remove index

labels = df['Scores'].values


import matplotlib.pyplot as plt
plt.scatter(features,labels)
plt.xlabel('Hours spend')
plt.ylabel('Scores achieved')
plt.suptitle('Scores acheived vs time spent to prepare')

df.head #will give entire dataset
df.head() #will give first five dataset
type(features)
type(labels)
features.shape
labels.shape
features.ndim
labels.ndim

from sklearn.linear_model import LinearRegression

#create an object
regression = LinearRegression()
features = features.reshape(25,1)
labels = labels.reshape(25,1)
#model - regression
regression.fit(features, labels)
m = regression.coef_
c = regression.intercept_

#Method1:
x = 9
#y = mx + c
(m*x) + c
"""
x = 9
(m*x) + c
for prediction
"""

#Method2:
#Direct method for regression
regression.predict([[9]]) #[[9]] - used since we need 2D array

regression.predict(features)

plt.scatter(features, labels)
plt.plot(features, regression.predict(features))
