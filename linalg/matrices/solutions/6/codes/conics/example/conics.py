import matplotlib.pyplot as plt 
import numpy as np 
from coeffs import *
import subprocess
import shlex

x = np.linspace( 0.5,1.2) 
a=3
b = -np.sqrt(24)
c=2
 
y = a*x**2 + b*x + c
 
x_1 = ( np.sqrt(24)+np.sqrt(24 - 4*3*2))/(2*3)
x_2 = ( np.sqrt(24)-np.sqrt(24 - 4*3*2))/(2*3)
A = np.array([x_1,0])
B = np.array([x_2,0])
print(A,B)
plt.plot(A[0],A[1],'o')
plt.text(A[0]+0.03,A[1]+0.03,'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]-0.04,B[1]+0.03,'B')
plt.plot(x,y)
plt.title('Parabola  ')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()