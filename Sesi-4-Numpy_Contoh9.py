# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:35:46 2022

@author: 082793
"""

import numpy as np
data = np.array([1,2,3,4,5])

print("data :",data)
print("data[0] :",data[0])
print("data[1] :",data[1])
print("data[0:2] :",data[0:2])
print("data[1:] :",data[1:])
print("data[-2:] :",data[-2:])
print("data[:2] :",data[:2])
print("data[:-1] :",data[:-1])
print("data[:-2] :",data[:-2])

data2 = sorted(data,reverse=True)
print(data2)
print(data2[0:])

