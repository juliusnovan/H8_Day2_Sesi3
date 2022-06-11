# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:13:09 2022

@author: 082793
"""

import numpy as np

arrsplit = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                     [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])

print(arrsplit)

arsp = np.hsplit(arrsplit,4)

