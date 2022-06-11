# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:04:43 2022

@author: 082793
"""

import numpy as np

arr_1 = np.array([[1, 1],
     [2, 2],
     [3, 3]])

arr_2 = np.array([[4, 4],
     [5, 5],
     [6, 6]])

print(arr_1)
print(arr_2)
print(np.vstack((arr_1, arr_2)))
print(np.hstack((arr_1, arr_2)))
