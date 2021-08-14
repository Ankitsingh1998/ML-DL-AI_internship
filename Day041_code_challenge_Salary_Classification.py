#Day041 - code challenge Salary Classification
import pandas as pd
df = pd.read_csv('Salary_Classification.csv')

features = df.iloc[:,0:4].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
C_Transformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')

import numpy as np
features = np.array(C_Transformer.fit_transform(features), dtype = np.float32)
features = features[:,1:]

import statsmodels.api as sm

features = sm.add_constant(features)

features_optimized = features[:,[0,1,2,3,4,5]]

regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()

"""
#Method 1:
p_value = regression_ols.pvalues.tolist()

required_columns = []

for num in p_value:
    if num <= 0.05:
        required_columns.append(p_value.index(num))

features_optimized = features[:,required_columns] #After feature selection
#Not correct as it will remove all max pvalues columns directly
"""

#Method 2:
features_optimal = features[:, [0,1,2,3,4,5]]

while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, np.argmax(p_values), 1)
    else:
        break
#delete is used to delete an entire column and requires input array, sub-arrays to remove along the axis and then axis as 1 for entire column and 0 for row
#argmax returns index of maximum values along one axis
#argmin returns index of minimum values along one axis
print(features_optimal.shape)

"""
#Method 3:
old_column_list = [0,1,2,3,4,5]   
new_column_list = []
while True:
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05:
        new_column_list.append(np.argmax(p_values))
    else:
        break
#Runtime is too high
"""