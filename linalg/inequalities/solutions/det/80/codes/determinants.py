# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:47:30 2020

@author: Rubeena
"""
import numpy as np


a = 1
b = 2
c = 3

matrix1 = np.array([[3*a,-a+b,-a+c],[-b+a,3*b,-b+c],[-c+a,-c+b,3*c]])
print(matrix1)
det=np.linalg.det(matrix1)
print('Determinant is ', det)