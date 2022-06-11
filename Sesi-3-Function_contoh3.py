# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:33:05 2022

@author: 082793
"""

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the functionaaa: ", mylist)