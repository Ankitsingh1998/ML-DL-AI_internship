#Day035 - code challenge Box Office
#Version 1: only one feature and label
import pandas as pd
df = pd.read_csv('Box_Office.csv')
df.columns.tolist()

features = df['Days'].values
labels = df.iloc[:,1:].values

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
features = features.reshape(9,1)
regression.fit(features, labels)

day = int(input('Enter the day number to compare the box office collecton: '))
predicted = regression.predict([[day]])

bahubali_predicted, dangal_predicted = predicted[0]

if bahubali_predicted > dangal_predicted:
    print('So, Bahubali 2 will have more collections on the {0}th day '.format(day) + 'with a total collection of ' + str(bahubali_predicted.round(4)) + ' crores.')
else:
    print('So, Dangal will have more collections on the {0}th day '.format(day) + 'with a total collection of ' + str(dangal_predicted.round(4)) + ' crores.')

#Version 2: seperate labels
import pandas as pd
df = pd.read_csv('Box_Office.csv')
df.columns.tolist()

features = df['Days'].values
Bahubali2_labels = df.iloc[:,1:2].values
Dangal_labels = df.iloc[:,2:].values

from sklearn.linear_model import LinearRegression
regression1 = LinearRegression()
regression2 = LinearRegression()

features = features.reshape(9,1)
regression1.fit(features, Bahubali2_labels)
regression2.fit(features, Dangal_labels)

day = int(input('Enter the day number to compare the box office collecton: '))
Bahubali2_prediction = regression1.predict([[day]])
Dangal_prediction = regression2.predict([[day]])


if bahubali_predicted > dangal_predicted:
    print('So, Bahubali 2 will have more collections on the {0}th day '.format(day) + 'with a total collection of ' + str(bahubali_predicted.round(4)) + ' crores.')
else:
    print('So, Dangal will have more collections on the {0}th day '.format(day) + 'with a total collection of ' + str(dangal_predicted.round(4)) + ' crores.')
