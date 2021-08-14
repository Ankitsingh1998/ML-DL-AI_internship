#Functional programming - python
"""
map
filter
reduce
lambda
dictionary
tuple
"""

list1 = [1,2,3,4,5]
list2 = []
for item in list1:
    list2.append(item*item)
print(list2)

#list comprehension
squares = [item*item for item in list1]

list3 = ['Hi!','Hello!','Bye!']
length = [len(name) for name in list3]

#mapping 1.0
list4 = [10,20,30,40]

def squarefun(x):
    return x*x

print(squarefun(5))
print(list(map(squarefun,list4)))

#mapping 2.0
list5 = [0,1,2,3,4,5,6,7,8,9,10]
def is_even(x):
    if x%2==0:
        return 'even.'
    else:
        return 'odd.'

print(list(map(is_even,list5)))

for item in list5:
    print(item,'is',is_even(item))

def even(x):
    return (x%2==0)
#filter
print(list(filter(even,list5)))

#lambda function
print(list(filter(lambda x: (x%2==0),list5)))
print(list(map(lambda x: x**3,list5)))

#reduce and library functools
import functools
list6 = [2,3,4,5]
def power(x,y):
    return x**y
print(functools.reduce(power,list6))

#factorial
def mult(x,y):
    return x*y
print(functools.reduce(mult,[1,2,3,4,5]))

#Dictionary
"""
(key:value) pairs:
Name:Ranjan
Mat:87
Chem:78
Phy:71
"""
#Always unique keys
#Example 1.0
data1 = {
'Name':'Ranjan',
'Math':87,
'Chem':78,
'Phy':71
}

print(data1)
data1['Math']
data1['Chem']

data1['Chem'] = 85
data1['Chem']
data1
len(data1)
data1.keys()

del data1['Phy']
data1
data1.values()

for key in data1.keys():
    print(key)

dir(dict)
help(dict.update)

data1.clear()
data1

#Example 2.0
data2 = {
'Name':'Ranjan',
'Math':[34,38],
'Chem':[37,36],
'Phy':[32,31]
}

data2['Math'][0]
data2['Math'][1]

#Example 3.0
data3 = {
'Name':'Ranjan',
'Math':{'mid1':34,'mid2':38},
'Chem':{'mid1':37,'mid2':36},
'Phy':{'mid1':32,'mid2':31}
}

data3['Math']
data3['Math']['mid1']

#Example 4.0
#Nesting - dict in dict in dict.... (also for list)
data4 = {
'Name':'Ranjan',
'Math':{'mid':{'mid1':19,'mid2':24},'final':48},
'Chem':{'mid':{'mid1':18,'mid2':22},'final':46},
'Phy':{'mid':{'mid1':18,'mid2':21},'final':42},
}

data4['Chem']['mid']['mid1']
data4['Chem']['mid']['mid2']
data4['Chem']['final']
data4['Phy']['mid']
data4['Math']['final']

#tuple
divmod(31,6)
type(divmod(31,6))

#tuple unpacking
x,y = (5,1)
print('x is: ',x)
print('y is: ',y)

t1 = (13,15,16,19,11)
#tuples are read-only or immutable.
