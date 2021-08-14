#Day034 - code challenge cars
#Method 1:
import pandas as pd
df = pd.read_csv('cars.csv')
df.columns
df.shape

from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size = 0.4, random_state = 0)

df_train.to_csv('cars_train.csv', index=False)
df_test.to_csv('cars_test.csv',index=False)

df_train.columns
df_test.columns
df_train.shape
df_test.shape


#Method 2:
df2 = pd.read_csv('cars.csv')

features = df2.iloc[:, 1:].values
labels = df2.iloc[:, 0].values #price is the labels

#print (df2.columns.tolist())
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
df_features_train, df_features_test, df_labels_train, df_labels_test = train_test_split(features, labels, test_size = 0.4, random_state = 1)

df_features_train.to_csv('cars_features_train.csv',index=False)
df_features_test.to_csv('cars_features_test.csv',index=False)
df_labels_train.to_csv('cars_labels_train.csv',index=False)
df_labels_test.to_csv('cars_labels_test.csv',index=False)

