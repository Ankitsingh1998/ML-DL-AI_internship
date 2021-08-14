#Day042 - code challenge IQ Size
"""
Task01:
What is the IQ of an individual with a given 
brain size of 90, height of 70 inches, and weight 150 pounds ? 
"""
import pandas as pd
import numpy as np
df = pd.read_csv('IQ_Size.csv')

df.isnull().any(axis=0)

features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(features_train, labels_train)

prediction = regression.predict(features_test)
pd.DataFrame(zip(prediction.round(2), labels_test))

predicted_value = regression.predict([[90, 70, 150]])
print('For the given data of brain size 90, height of 70 inches & weight of 150 pounds, the IQ is found to be: '+str(predicted_value.round(2)))

"""
Task02:
Are a person's brain size and body size (Height and weight) predictive 
of his or her intelligence?
"""
#Method 1:
import statsmodels.api as sm

features_sm = sm.add_constant(features)

regression_ols = sm.OLS(endog = labels, exog = features_sm).fit()

print(regression_ols.summary())

features_optimized = features_sm[:,[0,1,2]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

features_optimized = features_sm[:,[1,2]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()

features_optimized = features_sm[:,[1]]
regression_ols = sm.OLS(endog = labels, exog = features_optimized).fit()
regression_ols.summary()
regression_ols.pvalues

print()
print('Intelligence depends mainly on Brain Size.')

#Method 2:
features_optimal = features_sm[:, [0,1,2,3]]
while (True):
    regression_ols = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regression_ols.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, np.argmax(p_values), 1)
    else: 
        break

features_optimal.shape
