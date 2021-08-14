#Day063 - code challenge NIRF rankings
NIRF = "https://www.embibe.com/exams/nirf-rankings/"

import requests
from bs4 import BeautifulSoup #to parse the data
import pandas as pd

source = requests.get(NIRF).text #reading html content

soup = BeautifulSoup(source, 'lxml') #html parsing

table = soup.find_all('figure', class_ = "wp-block-table")
#find_all --> finding all the tables with the same name

college_ranking_list =["NIRF Rankings Of Overall Educational Institutes.csv","NIRF Rankings Of Engineering Colleges.csv","NIRF Rankings Of Medical Institutes.csv","NIRF Rankings Of Universities.csv"]

#loops to read and convert each table into csv file
for i in range(len(table)):
    A=[]
    B=[]
    C=[]
    D=[]
    for body in table[i].find_all("tbody"):
        for row in body.find_all("tr"):
            col = row.find_all('td')
            A.append(col[0].text.strip())
            B.append(col[1].text.strip())
            C.append(col[2].text.strip())
            D.append(col[3].text.strip())
           

    df = pd.DataFrame(list(zip(A,B,C,D)), columns = ['Rank & Name of the institute', 'City', 'State', 'NIRF Score'])
    df.to_csv(college_ranking_list[i], index=False)


