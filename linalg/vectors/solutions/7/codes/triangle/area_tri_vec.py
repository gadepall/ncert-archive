#Code by GVV Sharma

#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *




#Line points
A = np.array([0,3,0]) 
B = np.array([0,-1,0]) 
C = np.array([2,1,0]) 

#Midpoints
D= np.add(A,B)/2
E=np.add(B,C)/2
F= np.add(A,C)/2

d = np.linalg.norm(E-F)
e = np.linalg.norm(D-F)
f = np.linalg.norm(D-E)

#Hero's formula
s = (d+e+f)/2
print(s,d,e,f)
area = np.sqrt(s*(s-d)*(s-e)*(s-f))
print("Hero's formula", area)

area = 1/2*np.linalg.norm(np.cross(E-D,F-D))
print("Cross Product", area)
