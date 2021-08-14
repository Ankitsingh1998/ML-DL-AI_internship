list1 = [1,2,3,4,5,6,7,]

type(list1)

dir(list)

list1.append(8)
print(list1)

list1[0]
list1[-1]

list1[0] = 11 #lists are mutable, i.e., it can be changed

print(list1)

list1.insert(2,50)
print(list1)

list1.remove(50)
print(list1)


list2 = [1,5,4,2,5,3,5,5,5,5,]
while (5 in list2):
    list2.remove(5)
print(list2)

list3 = ['hi','everyone','how','you','doin']

for char in list3:
    print(char)
#char is like a placeholder here for this iteration

list4 = [1,2,3,4,5,6,]
list5 = []
for num in list4:
    list5.append(num*num)
print(list5)

#list comprehension
new_item = [item*item for item in list4]
print(new_item)

list3 = ['hi','everyone','how','you','doin']
list4 = []
for char in list3:
    list4.append(char)

print([len(char) for char in list4])

#dictionary
"""
name--> Raghav
Standard --> 'Xth'
Math --> 85
Sci --> 82
"""

Student = {'Name' : 'Raghav',
'Standard' : 'Xth',
'Math' : 85,
'Sci' : 82
}

dir(dict)

print(Student['Sci'])
Student['Name'] = 'Raghav Raj'
Student['City'] = 'Pune'

print(Student)


#dict operations
import math
dir(dict)
help(dict.pop)

data_store2 = {}
while (True):
    b = input('Enter your number: ')
    if (not b):
        print('Invalid input. Please try again.')
        break #never terminates just skips the statement
    elif (b.isdigit()):
        b = int(b)
        data_store2[b] = math.sqrt(b)
    else:
        data_store2[b] = len(b)
print('Your previous records:\n',data_store2)















