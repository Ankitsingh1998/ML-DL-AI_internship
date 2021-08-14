#Day040 - Backward elimination for feature selection
import pandas as pd
df = pd.read_csv('Salary_Classification.csv')

df.shape
df.columns.tolist()
df.isnull().any(axis=0)
df.dtypes

features = df.iloc[:,0:4].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
C_Transformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')

import numpy as np
features = np.array(C_Transformer.fit_transform(features), dtype = np.float32)
features = features[:,1:]

#Backward Elimination
import statsmodels.api as sm
#statsmodels.api can be used instead of sklearn for linear regression
#OLS - optimal least square

features = sm.add_constant(features) #first column with every elements as 1
#Now, our data is ready to build the model
#fetaures, labels - no change in labels
features_optimized = features[:,[0,1,2,3,4,5]]
#created copy of a data so as to not bother our original data

regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()

#p value - to perform the backward elimination, deciding factor for the important columns
#higher the p value, lower the importance of that feature
#threshold - 5% (p value less than 0.05 will be considered only)
regression_ols.summary()
regression_ols.pvalues

#Now, start to drop columns with highest p value
features_optimized = features[:,[0,1,3,4,5]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

#Now drop column with next highest p value
features_optimized = features[:,[0,1,3,5]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

#Now drop column with next highest p value -we will perform this till we get each features/columns with p values less than 5%
features_optimized = features[:,[0,3,5]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

#Again, column with p value more than 5% will be eliminated
features_optimized = features[:,[0,5]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

"""
p value : probability that says your column by chance has come in the decision 
making process
"""
