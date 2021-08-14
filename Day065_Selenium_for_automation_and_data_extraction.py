#Day065 - Selenium for automation and data extraction
#Case 01
#Kerala results
from selenium import webdriver #selenium for automation/also for data scrapping

from time import sleep

url = "https://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

browser = webdriver.Chrome(executable_path="E:\Anaconda\chromedriver") #will open an empty chrome page on which we want to load our url programatically

browser.get(url) #link we want to load

sleep(2) #when entire code is run in one go, it's better to delay to load the page fully 

school_code = browser.find_element_by_name('treg') #to go into the school code entering box

school_code.send_keys('2000') #to pass the school code in our created page

sleep(2) #again, wait for few seconds

get_school_result = browser.find_element_by_xpath("//*[@id='ctrltr']/td[3]/input[1]")

get_school_result.click()

#now to extract data from this page
html_page = browser.page_source

from bs4 import BeautifulSoup as bs

soup = bs(html_page, 'lxml')

browser.quit()



#web scrapping using selenium
#Case 02
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    
from selenium import webdriver

browser = webdriver.Chrome(executable_path="E:\Anaconda\chromedriver") #will open an empty chrome page on which we want to load our url programatically

browser.get(wiki) #link we want to load
  
right_table = browser.find_element_by_class_name('wikitable') #to get the desired table

A = []
B = []
C = []
D = []
E = []
F = []
#find_elements_by_tag_name --> to search for the <td>, <th>, <tr> from the extracted html data
for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
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

