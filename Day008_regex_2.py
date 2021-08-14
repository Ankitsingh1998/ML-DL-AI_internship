#regex
import re
dir(re)
"""
sub
findall
search
match
compile
"""

mails = 'abc@gmail.com def@yahoo.com ghf@outlook.com'
#ABC@gmail.com, DEF@yahoo.com, GHIO@outlook.com
mail = re.sub(r'[abcdfeghi]+@','ABC@',mails) #re.sub needs pattern, then replacing character, then the string in which we are operating and then if want can provide count which will decide how many times we want to replace
print(mail)

str1 = '123abc123xyz456_0'
char = re.findall(r"\d{2}",str1) #re.findall returns all match inside a list with each match as a string and element of the list
print(char)

str1 = '123abc123def456_0'
char2 = re.findall(r"^\d{3}",str1)
print(char2)

str1 = 'a123abc123def456_0'
char2 = re.findall(r"^\d{3}",str1)
print(char2)

str2 = 'a123abc123def456_0bluepink'
char = re.findall(r"pink$",str2)
print(char)

str2 = 'pythondjango123_0'
char = re.search(r"\d{3}",str2) #search function - after first match will give result and stops searching

str3 = 'Forskforsk coding school'
re.match(r'forsk',str3)
re.match(r'Forsk',str3) #match - searches only in the beginning
re.search(r'forsk',str3)

#version 1.0
email_collection = 'abc123 abc123@gmail.com hg def@gmail.com ghf vdfcxg12jgh43@gmail.com hb helpdesk.it@gmail.com elses@gmail.in'
re.findall(r'[\w\.]+@\w+\.\w+',email_collection)

#version 2.0
email_collection = 'abc123 abc123@gmail.com hg def@outlook.com ghf vdfcxg12jgh43@gmail.com hb helpdesk.it@gmail.com elses@gmail.in gf hhdj mycode@yahoo.com'
my_pattern = re.compile(r'[\w\.]+@\w+\.\w+') #compile
new = my_pattern.findall(email_collection)

list1 = []
list1.append(new)
print(new)

print('a\tb')

print(r'a\tb')




