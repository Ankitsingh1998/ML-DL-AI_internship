#Day024 - code challenge baby names
import re
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

filenames = glob('*.txt')

#reading data from 1880 t0 2010 and adding a column named year
#concatenating all of the data into single dataframe
baby_list = []

i=1
while i<(2011-1879):
    file = 'yob'+str(1879+i)+'.txt'
    temp_df = pd.read_csv(file, names=['names', 'gender', 'counts'])
    year = int(re.findall(r'\d\d\d\d', file)[0])

    temp_df['year'] = year
    baby_list.append(temp_df)
    i+=1

df = pd.concat(baby_list, axis=0, ignore_index=True)

#Top 5 female and male baby names of the year 2010:
df_2010 = df[df['year']==2010]
female_names = df_2010[df_2010['gender']=='F']
sorted_females = female_names.sort_values('counts', ascending = False, ignore_index=True)
male_names = df_2010[df_2010['gender']=='M']
sorted_males = male_names.sort_values('counts', ascending = False, ignore_index=True)

print('Top 5 female baby names of the yaer 2010 are:\n', sorted_females['names'].head(5))
print('Top 5 male baby names of the yaer 2010 are:\n', sorted_males['names'][0:5])

#sum of the births column by gender as the total number of births in that year
yearly_grouping = df.groupby(['year','gender']).agg({'counts' : ['sum']})
print('Yearwise gender counts of babies:', yearly_grouping)

#Plot to show gender counts yearwise:
yearly_grouping.plot(kind='bar', stacked=False)
yearly_grouping.head(20).plot(kind='bar')

#For total male and female count since starting year to end year for whole data
total_males = df[df['gender']=='M']['counts'].sum()
total_females = df[df['gender']=='F']['counts'].sum()
