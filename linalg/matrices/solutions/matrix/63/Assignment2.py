# -*- coding: utf-8 -*-
"""
@author: Satyanarayana
"""
import numpy as np

A = np.array([[1,1,1],[1,1,1],[1,1,1]])
print("Matrix A = \n",A)
value = int(input("Please enter value of n(power):\n"))

B = np.linalg.matrix_power(A, value)

print("A^{} =\n{} ".format(value,B))

print("The value of 3^{} is {}".format(value-1,np.power(3,value-1)))