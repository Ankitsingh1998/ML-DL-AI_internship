#Day020 - code challenge baltimore
import pandas as pd
import numpy as nm
import matplotlib.pyplot as mt

file = pd.read_csv('Baltimore.csv')

file.columns.tolist()
#Removing the $ sign from annual salary field
"""
file.dtypes
type(file['AnnualSalary'])
"""
file['AnnualSalary'] = file['AnnualSalary'].astype(str)

file['AnnualSalary'] = file['AnnualSalary'].apply(lambda x: x.replace('$',''))

file['AnnualSalary'] = file['AnnualSalary'].astype(float)

#group te data jobtitle and annualsalary - groupby and agg
my_group = file.groupby(['JobTitle'])['AnnualSalary']
aggregate = my_group.agg([nm.sum, nm.mean])
print(aggregate)

#bar graph for different job roles
#version 1.0 - index and values
JobTypes = file['JobTitle'].value_counts()
JobRole = JobTypes.index[:10]
JobCount = JobTypes.values[:10]

fig1, ax1 = mt.subplots()
ax1.bar(JobRole, JobCount, label='Job Roles')
ax1.legend()

#version 2.0
file['JobTitle'].value_counts()[0:10].plot(kind = 'bar')

#To label the axis
mt.xlabel('Job Roles')
mt.ylabel('Number of employees')
mt.title('Employyes vs Their correspnding jobs')

mt.show()

#listing agency id and agency name - drop_dupllicates
agency_info = file[['Agency','AgencyID']]
agency_info.drop_duplicates(inplace=True)
print(agency_info)

#finding all missing data
#version 1.0
my_filter = file['GrossPay'].isnull()
len(file['GrossPay'][my_filter])
#version 2.0
my_filter.sum()
