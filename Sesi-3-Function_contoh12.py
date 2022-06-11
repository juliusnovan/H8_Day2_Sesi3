# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:17:41 2022

@author: 082793
"""

total = 0; 

def sum( arg1, arg2 ):

   total = arg1 + arg2; 
   print("Inside the function local total : ", total)
   return total;

def min():
    

    sum( 10, 20 );
print("Outside the function global total : ", total)