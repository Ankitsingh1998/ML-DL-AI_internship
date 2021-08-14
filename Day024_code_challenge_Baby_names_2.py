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

import numpy as np
x_val = []
for i in yearly_grouping.index:
    if i[0] not in x_val:
        x_val.append(i[0])
#Getting the count
yval = list(yearly_grouping['counts']['sum'])


#Female count are on even place
y_val_f = [yval[i]  for i in range(0,len(yval)) if i%2==0]
#Male count are on odd place

y_val_m = [yval[i]  for i in range(0,len(yval)) if i%2!=0]


  
X_axis = np.arange(len(x_val[0:10]))
  
plt.bar(X_axis - 0.2, y_val_f[0:10], 0.4, label = 'Female')
plt.bar(X_axis + 0.2, y_val_m[0:10], 0.4, label = 'Male')
  
plt.xticks(X_axis, x_val[0:10])
plt.xlabel("Year on axis, gender as plots")
plt.ylabel("number of children")
plt.suptitle('Baby counts yearwise')
plt.legend()
plt.show()
