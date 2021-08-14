#Day034 - code challenge Foodtruck
"""
import sklearn
dir(sklearn)
"""
import pandas as pd
df = pd.read_csv('Foodtruck.csv')
df.columns.tolist()

features = df['Population'].values
labels = df['Profit'].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.35, random_state = 2)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
features_train = features_train.reshape(63,1)
regression.fit(features_train, labels_train)

regression.predict([[3.073]]) #population in millions
"""
3.073 - scalar
[3.073] - array 1D
[[3.073]] - array 2D
"""

regression.predict([[33.4]]) #population in millions


features_test = features_test.reshape(34,1)
predicted = regression.predict(features_test)






