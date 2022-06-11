# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:33:44 2022

@author: 082793
"""

import numpy as np

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)


b = a.sum(axis=0)
print(b)


c = a.sum(axis=1)
print(c)


ones = np.ones(2)
print(ones)

print(a * a)

print(a * 2)

print(a.sum())

print(a.min())

print(a.max())

