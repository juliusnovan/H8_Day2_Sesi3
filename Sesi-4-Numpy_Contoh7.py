# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:07:30 2022

@author: 082793
"""


import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print(a.shape)

a2 = a[np.newaxis]
print(a2.shape)
print(a2)


row_vector = a[np.newaxis, :]
print(row_vector.shape)
print(row_vector)


col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)