# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:36:08 2020

@author: 91703
"""

import numpy as np
from numpy.core._multiarray_umath import ndarray
A = np.array([[1,-1,0,0],[2,0,1,0],[2,-1,0,0],[0,0,3,1]])
b = np.array([-1,5,0,13])
z = np.linalg.solve(A,b)
p = print(z)