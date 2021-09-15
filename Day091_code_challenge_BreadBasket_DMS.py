#Day091 - code challenge BreadBasket_DMS

"""
Code Challenge:
dataset = BreadBasket_DMS.csv

Q1. In this code challenge, you have given a dataset which has data 
and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, 
min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated 
item from given result row wise.

"""
#Draw the pie chart of top 15 selling items.

import pandas as pd
from apyori import apriori
from matplotlib import pyplot as plt
import numpy as np

# Data Preprocessing
df = pd.read_csv('BreadBasket_DMS.csv')

a = dict(df["Item"].value_counts())

items = []
values = []

i = 0
for x,y in a.items(): #key,values pairs appended in items and values list
    if i == 15:
        break #since, we need only top 15 items to visualise
    items.append(x)
    values.append(y)
    i += 1

#Visualisation - pie chart
explode = [0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0.05]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(values, labels = items,explode = explode, autopct='%1.2f%%')
plt.show()


#Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3
import pandas as pd
from apyori import apriori
# Data Preprocessing
# Column names of the first row is missing, header - None
df1 = pd.read_csv('BreadBasket_DMS.csv', header = None)

df1.drop([0],axis=0,inplace=True) #any row with value 0 will be dropped/deleted

df1[2] = df1[2].astype(int) #converting transactions into int object

transaction = []
value = 1
new = []
for j,i in enumerate(df1[2]):
    if i == value:
        new.append(str(df1.values[j,3]))
        value = i
    else:
        transaction.append(new)
        new = []
        new.append(str(df1.values[j,3]))
        value = i

#Now, applying apriori algorithm on the dataset
rules = apriori(transaction, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

print(type(rules))

results = list(rules)
print(len(results))

#Out of given results sets, show only names of the associated item from given result row wise.

for item in results:
    # first index of the inner list contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support = " + str(item[1]))

    #third index of the list located at 0th of the third index of the inner list

    print("Confidence = " + str(item[2][0][2]))
    print("Lift = " + str(item[2][0][3]))
    print("----------------------------------------")



