from math import sqrt
import numpy 
a=numpy.array([2,3,-1])
print("a is")
print(a)
b=numpy.array([1,-2,1])
print("b is")
print(b)
R=a+b
magR=numpy.linalg.norm(R)
print("resultant vector and its magnitude is")
print(R)
print(magR)
u = R/magR
print("unit vector along R is")
print(u)
A = 5*u
print("vector of magnitude 5 units along R is")
print(A)
