#Program to balance a chemical equation using echelon matrix

import numpy as np
import sympy


#if using termux
#import subprocess
#import shlex
#end if

#Coefficient Matrix
A= np.array([[1,2,0,-2], [1,0,-2,0], [3,2,-6,-1], [0,1,-1,0]])
#Row reduced echelon form
print("The row reduced echelon form of the matrix and pivot columns are: ")
print(sympy.Matrix(A).rref())
