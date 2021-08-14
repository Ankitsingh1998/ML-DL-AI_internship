#Day048 - 
import pandas as pd
df = pd.read_csv('Balanced_reviews.csv')

df.shape
df.columns.tolist()
df.head()
df.sample(10)
df['reviewText'].sample(5)
rating_counts = df['overall'].value_counts(normalize=True)
rating_counts.sum()

df.isnull().any(axis=0)

"""
#To find index numbers of any row with empty(nan) columns
tr = df.isnull().any(axis=1)
tr = tr.tolist()
tr.count(True)
tr.index(True)
list1 = []
for i in range(len(tr)):
    if tr[i] == True:
        list1.append(i)

list1 = pd.DataFrame(list1, columns=['index number'])

df.iloc[371,:] #nan value
"""

df.dropna(inplace=True)
df.shape
#792000 - df.shape[0] --> number of rows dropped

df[df['overall'] == 3]
df = df[df['overall'] != 3]
df.shape
df['overall'].value_counts()

import numpy as np

#np.where(condition, if condition is true it will return 1st value, else 2nd value)
df['positivity'] = np.where(df['overall'] > 3, 1, 0)
df.shape

df['positivity'].value_counts()
#where() uses vectorization, so even for large datset it will run fast.

#NLP - Natural Language Processing
