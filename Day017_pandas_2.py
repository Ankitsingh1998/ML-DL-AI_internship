#Day017 - pandas 2.0
#pandas DataFrame
#https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
import pandas as pd
dt = pd.read_csv('Salaries.csv')

dt.columns  #gives column names in array
dt['rank'] , dt['salary'] #gives both columns seperately
c1 = dt[['rank','salary']]  #gives columns together
print(c1)

percentage_unique = dt[input('Enter a column name: ')].value_counts(normalize=True)
print(percentage_unique)
print(percentage_unique*100,'%')

dt['discipline'].max()

dt.columns.tolist() #converts column names from array to list

dt['salary']
dt.salary #statements on lines 18 & 19 are same, but try to use the one on line 18

dt['rank']
dt.rank #error in expected output because rank is internal property of dataframe
#dt.rank gives entire rows*column

dt['salary'] > 110000 #gives output in boolean indexing
#above statement is kind of a filter

above_110000 = (dt['salary'] > 110000)
dt[above_110000]
len(dt[above_110000])

d1 = dt[dt['salary'] > 110000] #will filter and output the results which are satisfying the conditions
len(d1)

"""
gender_f = (dt['gender'] == 'Female')
dt(above_110000 & gender_f) #will show TypeError so we have to call new variable.
so we determine d2 seperately without using two different variables and then it will run.
"""

d2 = dt[(dt['salary'] > 110000) & (dt['gender'] == 'Female')]
print(d2)
len(d2)

dt.isnull() #checking missing data both column and row wise
dt.isnull().any(axis = 0) #checking missing data column wise
dt.isnull().any(axis = 1) #checking missing data row wise

"""
For row number of each nan/null data:
    d3 = dt.isnull().any(axis = 1).tolist()
    d4 = []
    for index_number in range(len(d3)):
        if d3[index_number] == True:
            d4.append(index_number)
    print(d4)              
"""
null_values = dt[dt.isnull().any(axis = 1)]
print(null_values)

#To fill the null values : fillna
dt['phd'].mean()
dt['phd'] = dt['phd'].fillna(round(dt['phd'].mean(), 1))
#fillna to fill for the null values

dt2 = dt.fillna(100) #will assign rest of nan values as 100

#dropna - to delete those rows with nan values
dt.dropna(inplace=True) 

#iloc - to get values for particular range of roos and columns
dt.iloc[1:9,3:] #will give data except 7th row and will add 8th row since previously we deleted that row

dt = pd.read_csv('Salaries.csv')

dt.iloc[1:9,3:]

dt.iloc[10,:] #particular row but entire column

dt.iloc[:,5] #particular column entire row

dt.iloc[[7,11],:] #for multiple different rows and all columns

dt.iloc[:,[2,3,5]] #for multiple different columns and all rows

