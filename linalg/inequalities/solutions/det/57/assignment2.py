#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:52:24 2020

@author: shantanu
"""
#assignment2

import numpy as np
from sympy import*  #to invoke sympy.matrix.rref() 


a = np.array([[5,-1,4],[2,3,5],[5,-2,6]])
b=np.array([5,2,-1]).reshape(3,1)
augM=np.column_stack((a,b))  #to write augmented matrix
print("The augmented matrix is :\n ",augM)

ech_augM=Matrix(np.column_stack((a,b))) 
echolon_augM = ech_augM.rref()

print("\n The echolon form of augmented matrix and the pivot elements are \n",echolon_augM)


x=np.linalg.solve(a,b)
print("\n The solution to the differential equations is: \n",x)