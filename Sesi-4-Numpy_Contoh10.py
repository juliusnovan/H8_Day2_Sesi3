# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:53:18 2022

@author: 082793
"""

import numpy as np

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)

# You can easily print all of the values in the array that are less than 5

print(a[a>=5])


five_up = (a >= 5)

print(a[five_up])
print(a[a>=5])


divisible_by_2 = a[a%2==0]

print(divisible_by_2)


c = a[(a > 2) & (a < 11)]

print(c)




