import numpy as np
import math as mt

def verify(X,Y):
    value=1
    if(len(X)!=len(Y) or len(X[0])!=len(Y[0])):
        print("Matrix Dimensions mismatched")
        value=0
    else:
        for i in range(len(X)):
            for j in range(len(X[0])):
                if(round( X[i][j],3)!=round( Y[i][j],3)):
                    value=0
    return value
    
theta=mt.radians(float(input("Enter the value of Alpha in Degrees ")))
A=np.array([[0,-mt.tan(theta/2)],[mt.tan(theta/2),0]])
B=np.array([[mt.cos(theta),-mt.sin(theta)],[mt.sin(theta),mt.cos(theta)]])
I=np.array([[1,0],[0,1]])
X=I+A
Y=(I-A)@(B)
print("LHS matrix is",X)
print("RHS matrix is",Y)
if(verify(X,Y)==1):
    print("LHS is same as RHS.Hence Proved")
else:
    print("LHS is not equal to RHS")






