"""
string operations
control flow
library/module import
looping
list
"""
str1 = "I already have completed python coding, just need some revision and practices."
print(type(str1))
print(len(str1))

#indexing, slicing
str1[0]
str1[-1]
str1[-2]
print(str1[:])
print(str1[:9])
print(str1[2:])
print(str1[2:9])
print(str1[2:14:3])
print(str1[-2:-12:-2])

#str_operation all functions
print(dir(str))
help(str.upper)
help(str.title)

#string operations
print(str1.upper())
print(str1.lower())
print(str1.title())
str2 = str1.upper()
print(str2)

""""
str1[0] = 'W'
strings are read-only or immutable
"""

#math library
import math
dir(math)
help(math.sqrt)
help(math.perm)
math.sqrt(20)
math.perm(5,3)
x = int(input('Enter a number: '))
print(math.sqrt(x))
print(math.perm(x,3))

"""condition is always true, kind of infinite looping
while (True):
    print('hello')
red button in console to stop infinite looping execution"""

"""x = ''
not x
True
x = 5
not x
False
"""
#vresion01
while (True):
    z = input('Enter another number: ')
    if (not z):
        print('Please provide a valid input.')
        break #terminate the loop
    elif (z.isdigit()):
        z = int(z)
        print(math.sqrt(z))
    else:
        print('Number cannot be letter/word/special character.')
        break

#version02
while (True):
    a = input('Enter your number: ')
    if (not a):
        print('Invalid input. Please try again.')
        continue #never terminates just skips the statement
    elif (a.isdigit()):
        a = int(a)
        print('The square root is',math.sqrt(a))
    else:
        print('Number cannot be letter/word/special character.')
        break



#list operations
dir(list)
help(list.copy)

data_store = []
while (True):
    b = input('Enter your number: ')
    if (not b):
        print('Invalid input. Please try again.')
        continue #never terminates just skips the statement
    elif (b.isdigit()):
        b = int(b)
        data_store.append(math.sqrt(b))
    else:
        print('Number cannot be letter/word/special character.')
        break
print('Your previous records:\n',data_store)


import math
#dict operations
dir(dict)
help(dict.pop)

data_store2 = {}
while (True):
    b = input('Enter your number: ')
    if (not b):
        print('Invalid input. Please try again.')
        continue #never terminates just skips the statement
    elif (b.isdigit()):
        b = int(b)
        data_store2[b] = math.sqrt(b)
    else:
        print('Number cannot be letter/word/special character.')
        break
print('Your previous records:\n',data_store2)








