#Day063 - BeautifulSoup

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
df = pd.DataFrame(list(zip(B, A, C, D, E, F)), columns=['State', 'Executive capital', 'Legislative capital', 'Judicial capital', 'Year of establishment', 'Former capital'])    

df.to_csv('List_of_states.csv', index=False)  #to save the dataframe as csv file

