# OOPs (Object Oriented Programming)
"""
Code Challenge 1
  Filename:
      radio.py
      Create a Radio class with characteristics and functionality discussed in class
      Create the object of the Radio class and start the radio and play a song

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------
Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)

I should be able to 
Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""

"""
Represent Employee in python:
    Individual employees will have special attributes and methods:
        Name - FirstName and LastName 
        Email - FirstName.LastName@company.com
        Pay
        4 attributes - FirstName, LastName, Email & Pay
        
                  Instance/object
                       /  \
                      /    \
                     /      \
                    /        \
               variables    Methods
               
Instance variable/class variable
Instance method/class method

                       class
                       /  \
                      /    \
                     /      \
                    /        \
               variables    Methods

class - blueprint on which basis actual objects forms which we call instances.
class variables - variables which are shared among all the instance of the class.
class variable should be same for all the instances of the class.
Instance - inside heap and will take memory for each instances.
"""


class Employee:
    pass


emp_1 = Employee()  # constructor
emp_2 = Employee()  # constructor
print(emp_1)
print(emp_2)
print(id(emp_1))
print(id(emp_2))


class Emp:
    def __init__(self):  # dunder methods
        print("Inside Employee constructor")


emp__1 = Emp()
print(emp__1)
emp__2 = Emp()
print(emp__2)


class Employees:
    #class variable - here, we define for our class variables
    num_of_emp = 0
    def __init__(self, first, last, salary):
        #self.num_of_emp is wrong to call class variable.
        #Instance variables:
        self.FirstName = first
        self.LastName = last
        self.Pay = salary
        self.Email = (first.lower() + '.' + last.lower() + '@forsk.ac.in')
        self.annual_income = ('Annual income of ' + self.FirstName +' ' + self.LastName + ' is ' + str(salary*12) + '.')
        Employees.num_of_emp += 1
        
    # Instance method:
    def fullname(self):
        return self.FirstName + ' ' + self.LastName

    def sal_per(self, n):
        return 'Salary of '+self.FirstName+' '+self.LastName + ' for ' + str(n) + ' months is: ' + str(self.Pay*n)+'.'


emp1 = Employees('Sylvester', 'Fernandes', 80000)
emp2 = Employees('Yogendra', 'Singh', 75000)
print(emp1.Email)  # print(emp1)
print(emp2.Email)  # print(emp2)
print(emp1.Pay)
print(emp1.annual_income)
print(emp1.fullname) 
"""
print(emp1.fullname) --> function not called so will not get 
the required output but since it stores the memory of that 
function so it will be shown.
"""
print(emp1.sal_per(6))
print(emp2.sal_per(6))
print(emp2.fullname())
#emp1 and emp2 are known as reference variables.
#emp1 is pointing towards sylvester object.
#emp2 is pointing towards yogendra object.
#2nd method to call instance method:
print(emp1.fullname())
print(Employees.fullname(emp1))
print(Employees.num_of_emp)


#Inheritance:
    
#Manager - Developer are subclass or child class or derived class
#Employees is superclass or parent class or base class
class Developer(Employees):
    pass

class Manager(Employees):
    pass

print(issubclass(Developer,Employees))
print(issubclass(Manager,Employees))
print(issubclass(Employees,Developer))

dev = Developer('Sylvester', 'Fernandes', 80000)
mng = Manager('Yogendra', 'Singh', 75000)

print(dev.fullname())

print(isinstance(dev,Developer))
print(isinstance(dev,Manager))
print(isinstance(mng,Manager))
print(isinstance(dev,Employees))
print(isinstance(mng,Employees))
print(isinstance(emp1,Manager))
print(isinstance(emp1,Developer))




#Multiple inheritance:
class A:
    pass
class B:
    pass
class C(A,B):
    pass

#Multi-level inheritance:
class D:
    pass
class E(D):
    pass
class F(E):
    pass

#python does noy have access modifiers concept.
#There is no concept of modes in python (private, protected, public).
#All members in a python class are public by default.
"""
variable public
_variable_ protected concept
__variable__ private
"""

#overloading and overadding concept is there in python.








