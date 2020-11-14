import numpy as np
from scipy import linalg
from sympy import symbols
#taking x as 1
x=1
theta=50
#even on changing values of theta the value of determinant is not changing
A=[[x,np.sin(theta),np.cos(theta)],[-np.sin(theta),-x,1],[np.cos(theta),1,x]]
print(linalg.det(A))
