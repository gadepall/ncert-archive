
#EE5609:Matrix Theory
#Assignment 2 
#Matrix exercises(3.9,12(i))
#Code by Sneha Konduru
#Roll no: ee19acmtech11009

#Libraries
import numpy as np
from sympy import *
from sympy.abc import a, b

# given problem
A= np.array([[a,b],[-b,a]])+np.array([[a,b],[b,a]])

print("result=",A)
