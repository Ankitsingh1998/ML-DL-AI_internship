#Day091 - apriori
import pandas as pd
from apyori import apriori

#column names - missing, no header, header - None
df = pd.read_csv('Market_Basket_Optimisation.csv', header=None) #Data preprocessing

df.shape

#df.isnull().any(axis=0) --> not a csv file with row and columns. so, invalid. 

#print([str(df.values[1,j]) for j in range(20)])
#print([str(df.values[1,j]) for j in range(20) if (type(df.values[1,j]) is not float)])
#type(nan) --> first use 'from numpy import nan'

#type(df.iloc[1,2]) --> str
#type(df.iloc[1,3])--> float

transactions = []
for i in range(0, 7501):
    #transactions.append(str(df.iloc[i,:].values)) #will give list inside list but as a string or without using str it will give numpy array
    #transactions.append([list(df.iloc[i,].values) for j in range(0, 20) if (type(df.values[i,j])) is not float]) --> will work but nana values acn't be replaced
    transactions.append([str(df.values[i,j]) for j in range(0, 20) if (type(df.values[i,j])) is not float])

#Now, training apriori algorithm on the dataset(df) --> will give a generator
rules = apriori(transactions, min_support = 0.0038, min_confidence = 0.25, min_lift = 4)

items = list(rules)

print(items)
print(items[0])

"""
min_support(s) --> In that week, atleast an item been sold 4 times a day which is equal 
to 4*7=28 times a week, s = 28/7501
min_confidence(c) --> If x is sold 100 times then y should be sold c times with x.
min_lift --> >1, strongly associated items
"""

"""
#Shortcut to write a generator
q = (i**2 for i in [1,2,3,4,5]) #() --> to create a generator & [] to create a list comprehension
print(type(q)) #type --> generator object
next(q) #iterator
p = list(q) #converts generator object to a list 
print(p) #will give generator as a list
"""

#Now, visualising the generator object as a list object
print(len(items))

#list of items
items[0].items
items[0][0]

#support
items[0].support 
items[0][1]  #support at index 1

#Ordered Statistics
items[0][2] #ordered statistics at index 2 --> as a list with one item --> OrderedStatistic
items[0][2][0] #OrderedStatistic
items[0][2][0].confidence #confidence at [0][2][0] - 3D, inside OrderedStatistic
items[0][2][0][2] #Confidence
items[0][2][0].lift #lift at [0][2][0] - 3D, inside OrderedStatistic
items[0][2][0][3] #Lift

for list1 in items:
    #first index of the inner list
    pair = list1[0] 
    item_list = [x for x in pair]
    print("Rule: " + item_list[0] + " -> " + item_list[1]) #relation between list items

    #second index of the inner list
    print("Support = " + str(list1[1]))

    #third index of the list located at 0th of the third index of the inner list
    print("Confidence = " + str(list1[2][0][2]))
    print("Lift = " + str(list1[2][0][3]))
    print("-------------------------------------------------------")