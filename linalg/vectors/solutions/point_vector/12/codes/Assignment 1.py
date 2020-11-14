#Python code for finding a unit vector parallel to given vector
import numpy as np
a=np.array([1,1,1])
b=np.array([2,-1,3])
c=np.array([1,-2,1])
#Given Vector is 2a-b+3c
d=2*a-b+3*c
#Finding magnitude of given vector (let's say "d")
e=np.linalg.norm(d)
"""Dividing magnitude of given vector with each values of vector
   to get a unit vector"""
f=(1/e)*d
# f is the resultant unit vector parallel to given vector
print(f)

