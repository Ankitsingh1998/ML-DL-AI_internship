#Day_009 - coding chalenge Simpson phonebook
#version 1.0
import re
ph = open("simpsons_phone_book.txt","r")
phonebook = ph.readlines()
pattern = r"^J[\w]*[\s]*(Neu)"

for contacts in phonebook:
    if (re.search(pattern, contacts)):
        print(contacts)
        
ph.close()



#version 2.0
import re
phonebook = open("simpsons_phone_book.txt","r")

pattern = r"^J[\w]*[\s]*(Neu)[\s]*[\d\-]+"

for contacts in phonebook:
    if (re.search(pattern, contacts)):
        print(contacts)
        
phonebook.close()


"""file handling -
read
readline
readlines


fh = open('simpsons_phone_book.txt', 'r')

fh.read()
fh.readline() #reads one line at a time
fh.readline()
fh.readlines() #reads each line in the form of a list

fh.close()
"""

"""
fh = open('simpsons_phone_book.txt', 'r')

for line in fh:
    print(line)        #will give output one line at a time by iteration
"""






