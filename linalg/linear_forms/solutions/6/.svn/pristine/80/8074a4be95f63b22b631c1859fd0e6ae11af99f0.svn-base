import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A = np.array([0,0])
B = np.array([0,1])
C = np.array([3/4,1])

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_AC = line_gen(A,C)

plt.plot(x_AB[0,:],x_AB[1,:],label='Width of the river')
plt.plot(x_BC[0,:],x_BC[1,:],label='Distance covered down the river')
plt.plot(x_AC[0,:],x_AC[1,:],label='Actual distance covered by the man')

plt.text(A[0]-0.02 , A[1] , 'A')
plt.text(B[0]-0.02 , B[1] , 'B')
plt.text(C[0]+0.01 , C[1] , 'C')
plt.title("The man and the river")
plt.legend()
plt.show()
