# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:01:05 2020

@author: pooja
"""

#%%
import sympy as sp

#%%
# To find the determinant of a matrix in algebraic form
x = sp.var('x')
y = sp.var('y')
A = sp.Matrix([[x, y, x+y], [y, x+y, x], [x+y, x, y]])
det_A = sp.det(A)
print("\n The given matrix A is:")
print(A)
print("\n The determinant of a given matrix is:")
print(det_A)

#%%
#To compute the determinant of a matrix
print("\nThe determinant of A for x=2 and y=3 is:")
print(det_A.subs(x, 2).subs(y, 3))
