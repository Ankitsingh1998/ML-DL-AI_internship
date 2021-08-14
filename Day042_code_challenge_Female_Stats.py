#Day042 - code challenge Female Stats
"""
task01:
Build A Predictive Model And Conclude If Both Predictors 
(Independent Variables) Are Significant For A Students’ Height Or Not?
(Use pvalue concepts).
"""
import pandas as pd
df = pd.read_csv('Female_Stats.csv')

df.columns
df.isnull().any(axis=0)

features = df.iloc[:,1:].values
labels = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(features_train, labels_train)

prediction = regression.predict(features_test)
print(pd.DataFrame(zip(prediction.round(2), labels_test)))

import statsmodels.api as sm

features_sm = sm.add_constant(features)

regression_ols = sm.OLS(endog = labels, exog = features_sm).fit()

print(regression_ols.summary())

"""
task02:
When Father’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Mother’s Height.
"""
print('Change in student\'s height when her mom\'s height is changed by 1 unit is: '+str(regression.coef_[0]))

"""
task03:
When Mother’s Height Is Held Constant, 
The Average Student Height Increases 
By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
print('Change in student\'s height when her father\'s height is changed by 1 unit is: '+str(regression.coef_[1]))
