#Day018 - numpy and matplotlib
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for item in list1:
    list2.append(item*10)
print(list2)

list3 = [item*10 for item in list1]

list1 = [1,2,3,4,5,6,7,8,9,10]

import numpy as np

x = np.array(list1)
type(x) #collection - ndarray
x[0] #print as list, indexing is there too
x[2:6] #slicing similar to list
type(x[0]) #int32

#dt.unique() --> ndarray in Day016

x.shape #dimension
x.ndim #dimension

#Vectorization
#Array
#For scalar value:
y = 5 
y = np.array(y)
type(y)
y.shape
y.ndim

#1D array:
z = [5]
type(z)
z = np.array(z)
z.shape
z.ndim

#2D array:
z = [[5]]
type(z)
z = np.array(z)
z.shape
z.ndim

#2D array:
z = [[1,3,5],[2,4,6]]
type(z)
z = np.array(z)
z.shape
z.ndim

#3D array:
z = [[[1,3,5],[7,9,11]],[[2,4,6],[8,10,12]]]
type(z)
z = np.array(z)
z.shape
z.ndim

list1 = [1,2,3,4,5,6,7,8,9]
np.array(list1)
x = x.reshape(3,3)
x.shape
#np.arange(10)
y = np.arange(5, dtype = np.int64)
type(x[0])

np.ones((2,3)) #dot in result due to float datatype
np.ones((3,2), dtype = np.int64) #ndtype = np.int8/16/32/64converts into integer

np.zeros((2,5))
np.zeros((2,5), dtype = np.int8)


import matplotlib.pyplot as mt
x = [1,2,3,4,5]
y = [1,2,3,4,5]
mt.scatter(x,y) #scatterplot
mt.plot(x,y) #straight line plot

z = np.arange(20)
a = [i**3 for i in z]

mt.scatter(z,a)
mt.plot(z,a)
mt.scatter(a,z)
mt.plot(a,z)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
engineering_department = ['CSE','Petroleum','Chemical','EE','Civil','Mechanical','IT','ECE']
student_number = [42,38,41,37,36,28,48,40]
margin = (0,0.2,0.1,0,0,0,0,0) #only explodes Petroleum

fig1, ax1 = mt.subplots()
ax1.pie(student_number, explode=margin, labels=engineering_department, autopct='%.2f%%',
        shadow=True, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
mt.show()

#For more on numpy arrays:
#https://numpy.org/doc/stable/reference/arrays.indexing.html

#For any type of plot/graph visit matplotlib here:
#https://matplotlib.org/stable/gallery/index.html

import numpy as np
list1 = [1,2,3,4,5,6,7,8,9,10]
list1[-3:-8:-1]
arr = np.array(list1)
arr[-8:-3]