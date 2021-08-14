#Day045 - Polynomial Regression
import numpy as np
import pandas as pd
df = pd.read_csv('Claims_Paid.csv')

df.columns
#df['Year'].head(5)

#df['Year'] = df['Year'] - df['Year'][0]
#df.head()
df.dtypes
df.isnull().any(axis=0)

features = df.iloc[:,[0]].values
labels = df.iloc[:,1].values

import matplotlib.pyplot as plt
plt.scatter(features, labels, c='r')

from sklearn.linear_model import LinearRegression
rgr = LinearRegression()

rgr.fit(features, labels)

rgr.predict([[1981]])

#plot original vs predicted
labels_predicted = rgr.predict(features)

plt.style.use('classic')
plt.scatter(features, labels, c='r', label='original data')
plt.plot(features, labels_predicted, c='k', label = 'predicted line')
plt.xlabel('Year')
plt.ylabel('cost')
plt.legend()
plt.title('Claims_paid')
plt.suptitle('Years vs Cost')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
pol_rgr = PolynomialFeatures(degree=5)

features_ndata = pol_rgr.fit_transform(features)

rgr_ndata = LinearRegression()
rgr_ndata.fit(features_ndata, labels)

plt.scatter(features, labels, c='r', label='original data')
plt.plot(features, rgr_ndata.predict(pol_rgr.transform(features)), c='k', label = 'predicted polynomial')
plt.xlabel('Year')
plt.ylabel('cost')
plt.legend()
plt.title('Claims_paid')
plt.suptitle('Years vs Cost')
plt.show()

#Now, predict for the year 1981
rgr_ndata.predict(pol_rgr.transform([[1981]]))

"""
Note:
1. Data standardization is the process of rescaling the attributes so that 
they have mean as 0 and variance as 1.
2. The ultimate goal to perform standardization is to bring down all the features 
to a common scale without distorting the differences in the range of the values.
3. In sklearn.preprocessing.StandardScaler(), centering and scaling happens 
independently on each feature.

fit_transform():
fit_transform() is used on the training data so that we can scale the training 
data and also learn the scaling parameters of that data. Here, the model built 
by us will learn the mean and variance of the features of the training set. 
These learned parameters are then used to scale our test data.
The fit method is calculating the mean and variance of each of the features 
present in our data. The transform method is transforming all the features 
using the respective mean and variance.
Now, we want scaling to be applied to our test data too and at the same time 
do not want to be biased with our model. We want our test data to be a 
completely new and a surprise set for our model. The transform method helps us 
in this case.

transform():
Using the transform method we can use the same mean and variance as it is 
calculated from our training data to transform our test data. Thus, the 
parameters learned by our model using the training data will help us to 
transform our test data.

If we will use the fit method on our test data too, we will compute a new mean 
and variance that is a new scale for each feature and will let our model learn 
about our test data too. Thus, what we want to keep as a surprise is no longer 
unknown to our model and we will not get a good estimate of how our model is 
performing on the test (unseen) data which is the ultimate goal of building a 
model using machine learning algorithm.
This is the standard procedure to scale our data while building a machine 
learning model so that our model is not biased towards a particular feature 
of the dataset and at the same time prevents our model to learn the 
features/values/trends of our test data.
"""

