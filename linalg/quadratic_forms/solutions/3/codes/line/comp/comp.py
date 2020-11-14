
#Prob  47 of exercise 8.1
#code by Krishnaja Kodali
#proof that a line parallel to parallel sides of a trap  divides the non parallel sides in equal ratio
import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *
#using termux
#import subprocess
#import  shlex
#def destroy(self):

a=2
b=-3
D1 = np.array([1,0])
M1 = np.array([[a,-b],[b,a]])
M1inv=np.linalg.inv(M1)
A=M1inv@D1
print("Multiplicative inverse of complex number is ")
print(A)

print(A[0]*a-b*A[1])
print(b*A[0]+a*A[1])

