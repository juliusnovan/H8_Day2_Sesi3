# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:29:46 2022

@author: 082793
"""

import numpy as np

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)

# You can create a new array object that looks at the same data

b = a.view()
print(b)


