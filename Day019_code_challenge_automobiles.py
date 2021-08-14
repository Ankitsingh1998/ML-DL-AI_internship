#Day019 - code challenge EDA(Exploratory Data Analysis)
import pandas as pd
import matplotlib.pyplot as mt

file = pd.read_csv('Automobile.csv')
"""
file.columns.tolist()
file['price']
file.isnull().any(axis=0)
file.dtypes
file['price'] = file['price'].astype(float)
"""
#filling null values of price column
file['price'] = file['price'].fillna(file['price'].mean())

#price column to ndarray
price_array = file['price'].values

#min, max, mean and ssd of price
print('Minimum price value is:',file['price'].min())
print('Maximum price value is:',file['price'].max())
print('Average/mean price value is:',round(file['price'].mean(),2))
print('Standard deviation value for price is:',round(file['price'].std(),2))

#pie chart for all car makers
company = file['make'].value_counts()
top_manufacturers = company.index[:11]
vehicle_number = company.values[:11]
margin = [0.1,0,0,0,0,0,0,0,0,0,0.2]
fig1, ax1 = mt.subplots()
ax1.pie(vehicle_number, explode=margin, labels=top_manufacturers, autopct='%.2f%%',
        shadow=True, startangle=0)
ax1.axis('equal')
mt.show()









