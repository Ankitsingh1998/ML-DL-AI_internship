#Day036 - Imputer from sklearn to handle missing values
"""
#score - accuracy (How much accurate our mpodel is??)
#train score
regression.score(features_train, labels_train)

score uses this:
    First, predict(features_train)
    then, compare with labels_train

#test score
regression.score(features_test, labels_test)
"""

import pandas as pd
from numpy import nan

players = pd.read_csv('cricket_salary_data.csv')
players.columns.tolist()
"""
players.isnull().any(axis=0)
players['Age'].fillna(np.mean(players['Age']))
"""

#Imputation - handling the missing data
#Simple Imputer - sklearn to fill null values
features = players.iloc[:,0:3].values

labels = players.iloc[:,3].values #3 or -1 for last index
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = nan, strategy = 'mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2]) 
#fit_transform - method to handle missing values

#directly filling missing values into our dataframe
players['Age'] = imputer.fit_transform(features[:,1:2]).round(2)
