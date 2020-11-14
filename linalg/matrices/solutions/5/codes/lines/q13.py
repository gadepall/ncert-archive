# 3*4 matrix
#Aij = 1/2 |-3i+j|
A=[]
import numpy as np
for i in range(3):
    B=[]
    for j in range(4):
        B.append(abs(-3*i+j)/2)
    A.append(B)
print("The required matrix is",A)

# 3*4 matrix
#Aij = 2i-j
C=[]
import numpy as np
for i in range(3):
    D=[]
    for j in range(4):
        D.append(2*i-j)
    C.append(D)
print("The required matrix is",C)
