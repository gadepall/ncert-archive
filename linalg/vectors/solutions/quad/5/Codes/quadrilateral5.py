import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


A = np.array([-2,-1])
B = np.array([4,0])
C = np.array([3,3])
D = np.array([-3,2])

vec_AB=A-B
vec_BC=B-C
vec_DC=D-C
vec_AD=A-D

print(vec_AB)
print(vec_DC)
print(vec_BC)
print(vec_AD)

x_AB=line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label="AB")

x_BC=line_gen(B,C)
plt.plot(x_BC[0,:],x_BC[1,:],label="BC")

x_CD=line_gen(C,D)
plt.plot(x_CD[0,:],x_CD[1,:],label="CD")

x_AD=line_gen(A,D)
plt.plot(x_AD[0,:],x_AD[1,:],label="AD")



#plotting point
plt.plot(A[0],A[1],'.')
plt.plot(B[0],B[1],'.')
plt.plot(C[0],C[1],'.')
plt.plot(D[0],D[1],'.')

plt.text(A[0]*(1+0.15),A[1]*(1+0.15), "A", color='red')
plt.text(B[0]*(1+0.03),B[1]*(1-0.15), "B", color='red')
plt.text(C[0]*(1+0.03),C[1]*(1+0.01), "C", color='red')
plt.text(D[0]*(1+0.04),D[1]*(1+0.05), "D", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.xlim(-4,6)
plt.legend(loc='upper right');plt.grid();


