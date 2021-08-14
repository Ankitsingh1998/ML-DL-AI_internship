#Day030 - code challenge thanksgiving
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
df = pd.read_csv('thanksgiving.csv', encoding='Windows 1252') #encoding in Windows 1252

df.columns #in array format
column_name = df.columns.tolist() #in list format

#replace column names by number codes
df.shape
column_codes = [i for i in range(65)] #Initializing codes for each columns
column_code_mapping = dict(zip(column_codes, column_name)) #zip for mapping - to store column names with number codes
df.columns = column_codes #column names changed to number codes
print(df.columns)
#respondants who celebrates thanksgiving
df[1].value_counts()
celebrate_thanksgiving = df[df[1]=='Yes']
celebrate_thanksgiving.count(axis=1)
celebrate_thanksgiving.shape
print(celebrate_thanksgiving.shape[0])

#check missing values
df.isnull().any(axis=1)
df.isnull().any(axis=0)
df = df.replace(np.nan, 'Missing') #to replace nan with missing

# Analysing for the state/region, area  and income based what is consumed in thankgiving dinner
region_based = df.groupby(64)
region_based.groups #to get same regions for different indexes
print(region_based.size()) #to get total similar regions, works as count

income_based = df.groupby(63)
income_based.groups
print(income_based.size())

area_based = df.groupby(60)
area_based.groups
print(area_based.size())

#Analysis of the sauces preffered by each income groups people
sauce_type_income_group = df.groupby(8)[63]
sauce_type_income_group_percentage_conversion = sauce_type_income_group.value_counts(normalize=True)
print(sauce_type_income_group)

#Gender conversion to numeric values. (Male == 0, Female == 1)
# Filtering the gender and income columns using .apply method
def gender_filtration(gender):
    if gender == 'Male':
        gender = 0
    elif gender == 'Female':
        gender = 1
    
    return gender

df[62] = df[62].apply(gender_filtration)
df[62].value_counts(dropna=False)

#cleaning income
df[63].value_counts()
df[63] = df[63].replace(['Prefer not to answer', 'Missing'],['0','0'])
regex = re.compile("\d+\W*\d+")
# A function to be passed in .apply() method for filtering out the salaries
def income_filter(value):
    value = regex.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)

df[63] = df[63].apply(income_filter)
#print((75000+99999)/2)
#print((75000+99999)/(2+0.1))

#fetching average income for each type sauces
sauce_type_income = df.groupby(8)[63]
sauce_type_income.groups
average_sauce_type_income = sauce_type_income.mean()
print(average_sauce_type_income)

#Visualizing the average income for each type sauces
average_sauce_type_income.plot(kind='bar', legend=True, stacked=False, color='#1970E7')
plt.xlabel('sauces')
plt.ylabel('income')    
plt.suptitle('average income for each type sauces for 2015 thanksgiving')
