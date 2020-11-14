#EE5609:Matrix Theory
#Assignment 1 (using directional vector and inner product)
#Lines and Planes(Prob.39)
#Code by Sneha Konduru
#Roll no: ee19acmtech11009

#Libraries
import numpy as np
from sympy import *
from sympy.abc import h
from sympy import solve

#Given Points A,B. 
A=np.array([h, 3])
B=np.array([4, 1])

#Given line equation 7x-9y=19
Line=np.array([7, -9, -19])

xcoefficient=Line[0]
ycoefficient=Line[1]

#Directional vector for two points and line equation
dirctionalVec1= B - A
dirctionalVec2=np.array([ycoefficient, -xcoefficient])

print("directional vector of points A and B:",dirctionalVec1)
print("directiol vector of line 7x-9y=19 is:",dirctionalVec2)

#Computing Inner Product
InnerProduct=np.inner(dirctionalVec1,dirctionalVec2)

#Computing h value
h=solve(InnerProduct)          

print("Inner Product of Two directional vectors:",InnerProduct)
print("value of h:",h)

