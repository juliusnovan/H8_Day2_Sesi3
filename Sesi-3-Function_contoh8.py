# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:17:00 2022

@author: 082793
"""

# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )
printinfo( name="adi")



# Function definition is here
def printinfo(name, age = 26,gender = "male"):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   print("gender: ", gender)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )
printinfo( name="adi", gender="female")
printinfo( name="budi")



def coba(variable):
    variable = 'berubah'
    return variable;
    
var2 = '123'
print(var2)
var2 = coba(2)
print(var2)


