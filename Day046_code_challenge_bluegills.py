#Day046 - code challenge bluegills
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')

df= pd.read_csv('bluegills.csv')
df.columns.tolist()

features = df.iloc[:,[0]].values
labels = df.iloc[:,[1]]

df.isnull().any(axis=0)
plt.scatter(features, labels, c='r')

from sklearn.linear_model import LinearRegression
rgr = LinearRegression()
rgr.fit(features,labels)

prediction_with_LR = rgr.predict([[5]])

labels_predicted = rgr.predict(features)

features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape(len(features_grid), 1)

grid_prediction = rgr.predict(features_grid)

plt.scatter(features, labels, c='r', label='original data')
plt.plot(features_grid, grid_prediction, c='k', label = 'predicted line')
plt.xlabel('Age of the fish')
plt.ylabel('Length of the fish')
plt.legend()
plt.title('Bluegills')
plt.suptitle('Age vs length for bluegill fishes')
plt.show()

rgr.score(features, labels)

from sklearn.preprocessing import PolynomialFeatures
pol_rgr = PolynomialFeatures(degree = 2)

features_ndata = pol_rgr.fit_transform(features)

rgr_ndata = LinearRegression()
rgr_ndata.fit(features_ndata, labels)

plt.scatter(features, labels, c='r', label='original data')
plt.plot(features_grid, rgr_ndata.predict(pol_rgr.fit_transform(features_grid)), c='k', label = 'predicted polynomial')
plt.xlabel('Age of the fish')
plt.ylabel('Length of the fish')
plt.legend()
plt.title('Bluegills')
plt.suptitle('Age vs length for bluegill fishes')
plt.show()

rgr_ndata.score(features_ndata, labels)

prediction_with_PR = rgr_ndata.predict(pol_rgr.transform([[5]]))

print('Prediction by Linear Regression: '+str(prediction_with_LR[0][0].round(2))+'cm')

print('Prediction with Polynomial Regression: '+ str(prediction_with_PR[0][0].round(2))+'cm')
