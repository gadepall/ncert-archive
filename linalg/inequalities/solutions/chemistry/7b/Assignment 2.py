#Program to balance a chemical equation using echelon matrix

import numpy as np
import sympy as sp

A= np.array([[1,0,0,-1,] [0,1,-1,0], [0,0,1,-2], [0,0,3,-6]])
#Row reduced echelon form
print("The row reduced echelon form of the matrix and pivot columns are: ")
print(sp.Matrix(A).rref())