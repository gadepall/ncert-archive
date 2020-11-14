import matplotlib.pyplot as plt 
import numpy as np 
from coeffs import *
import subprocess
import shlex

x = np.linspace(-4.5,5)
a = 2
b = -1
c = 1/8
y = a*x**2 + b*x + c
x_1 = (-b+np.sqrt(b**2 - 4*a*c))/(2*a)
x_2 = (-b-np.sqrt(b**2 - 4*a*c))/(2*a)
A = np.array([x_1,0])
B = np.array([x_2,0])
print(A,B)
plt.plot(A[0],A[1],'o')
plt.text(A[0]+0.75,A[1],'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]-2,B[1],'B')
plt.plot(x,y)
plt.title('Parabola 4')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()