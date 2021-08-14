#Day064 - sqlite3
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    
import requests #get and post api
    
from bs4 import BeautifulSoup #Beautiful soup to parse the data

source = requests.get(wiki).text #to read the html content

soup = BeautifulSoup(source, "lxml") #'lxml' --> html parser
    
right_table = soup.find('table', class_ = 'wikitable sortable plainrowheaders')
#soup.find() --> to find the desired table
#class_ --> takes the table name from inspection section in html of webpage

A = []
B = []
C = []
D = []
E = []
F = []
#findAll --> to search for the <td>, <th>, <tr> from the extracted html data
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    #if first row, th(count) = 7, td(count) = 0
    #for rest of the rows, th(count) = 1, td(count) = 6
    if len(cells) == 6:  #to skip the first row
        A.append(cells[1].text.strip())  #strip --> to remove extra spaces
        B.append(states[0].text.strip()) #strip is optional
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd  #create into dataframe
df = pd.DataFrame(list(zip(B, A, C, D, E, F)), columns=['State', 'ExecutiveCapital', 'LegislativeCapital', 'JudicialCapital', 'YearOfEstablishment', 'FormerCapital'])    

df.to_csv('List_of_states.csv', index=False)  #to save the dataframe as csv file - dumping a data to a flat file system

import sqlite3 as sql
import pandas as pd

conn = sql.connect('List_of_states.db') #to make a connection 

df.to_sql('List_of_Indian_states', conn) #creates table inside the database (.db) / to write the data



#reading the data from the table with sql query
read_conn = sql.connect('List_of_states.db')
new_df = pd.read_sql('SELECT * FROM List_of_Indian_states WHERE YearOfEstablishment == 1956', read_conn)



#how to read the data one at a time
One_conn = sql.connect('List_of_states.db')

cursor = One_conn.cursor()

cursor.execute('SELECT * FROM List_of_Indian_states')

for record in cursor:
    print(record)

#for year_of_establishment 1956
cursor.execute('SELECT * FROM List_of_Indian_states WHERE YearOfEstablishment == 1956')

for record in cursor:
    print(record)

