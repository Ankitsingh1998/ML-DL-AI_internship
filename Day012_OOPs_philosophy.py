#OOPs philosophy:
"""
In C,
int i = 6
2 bytes of memory allocated in the stack area
"""
#In python:
#a is a reference variable
a = 6
print(a)
print(id(a))
#Heap & Stack - both memoy area in RAM
str1 = 'Keyaru'
print(id(str1))

b = 6
print(id(b))

str2 = 'Keyaru'
print(id(str2))

str3 = 'Keyargu'
print(id(str3))

#All data structures in python are classes
print(type(a))
print(type('K'))
print(type(True))
print(type(None))

"""History of software development:
    1950 - First OS (Assembly language)
    1960 - Fortran, Algol, Cobol, Basic
    1964 - OS/360 Mainframe
    Procedural language - routines/sub-routines/function nowadays
    different files (long projects - more files and vice-versa) - variables/functions
    slow,expensive and time consuming, multiple variables, multiple functions, multiple files and atorage more
    real world objects - Banks,jewellery,Retail
    (Non Procedural)
"""
"""
Maintainability
Extensibility
Reusibility
- OOPs came into action.
OOPs is a philosophy not a language.
It logically groups data(variables) and function.
"""
"""
    1967 - Simula (OOP)
    1970 - C/Unix
    1991 - Linux
"""
"""
OOPs:
Class - 
objet/instance - 
Data Hiding - 
Abstraction - 
Encapsulation - 
Inheritance - 
Polymorphism - 
Overriding - 
Overloading - 
"""
"""
Radio making - 1000 pieces
1) Design/Blueprint  -  Class
2) Manufacturing company - Design, logo, 1000 radio
3)1000 individual radio (object/instance)
    Every radio will be different but they will be similar.
"""
"""
Algorithm to convert any real world object into class
1) Visualise or study the real world object
2) List down the characteristics/attributes of a real world object
3) List down the behaviour/functionalities of a real world object
|-------|--------------------------------|------------------------------------|
| S.No. |characteristics                 |          functionalities           |
|-------|--------------------------------|------------------------------------|
| 1.    | color                          |                                    |
| 2.    | brand                          |                                    |
| 3.    | AC_power                       |                                    |
| 4.    | Headphone                      |                                    |
| 5.    | power_led                      | power_switch (ON/OFF)              |
| 6.    | mode_led                       | mode_switch (AM/FM)                |
| 7.    | frequency                      | band_tuner (88.0-108.0)            |
| 8.    | Volume                         | Volume_tuner (1-10)                |
|-------|--------------------------------|------------------------------------|
characteristics are mapped into data/variables.
Functionality are mapped into methods/functions.
class_name = Real world object name = Radio
8 variables
4 functions
Object/Instance
Radiop class - blueprint design
"""

#Employee: data,variables --> functions,methods
class Employee :
    #adding our data/variables
    #adding our methods/functions
    pass  #pass - keyword to pass the function, we don't know what to provide
#at the place of break, continue we can also provide pass.
emp_1 = Employee() 
#emp_1 is known as reference variable
#memory allocation in stack
#create an object of Employee in heap
#stores the address in the reference variable
print(id(emp_1))  #1892868868656  #<__main__.Employee object at 0x000001B8B7C6CA30>
#both are showing same address but .main is showing address at hexadecimal
emp_2 = Employee()
print(id(emp_2))  #1892868565792  #<__main__.Employee object at 0x000001B8B7C6CE20>

#OOPs - senior management tool - to design solution





