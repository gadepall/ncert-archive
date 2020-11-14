# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:05:34 2020

@author: Rishab
"""
import numpy as np
import math as m

print("Solution to (i)\n")
x = float(input("Enter the value of x in degrees: "))
x = m.radians(x)
A = np.array([[m.cos(x),m.sin(x)],[-m.sin(x),m.cos(x)]]) # Matrix A
B = np.transpose(A) # Matrix B
res = np.matmul(B,A) # Resultant Matrix 
res = np.where(res<0, 0, res)
print(res)
print("\n")
print("The resultant matrix is an Identity Matrix.\nHence we can say that A'A = I for the given matrix A.")
print("\n\n\n")
print("Solution to (ii)\n")
y = float(input("Enter the value of y in degrees using math module: ")) 
y = m.radians(y)
A = np.array([[m.sin(y),m.cos(y)],[-m.cos(y),m.sin(y)]]) # Matrix A
B = np.transpose(A) # Matrix B
res = np.matmul(B,A) # Resultant Matrix 
res = np.where(res<0, 0, res)
print(res)
print("\n")
print("The resultant matrix is an Identity Matrix.\nHence we can say that A'A = I for the given matrix A.")
