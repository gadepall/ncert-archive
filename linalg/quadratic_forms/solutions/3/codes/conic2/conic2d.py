import numpy as np
import matplotlib.pyplot as plt
import subprocess
import  shlex
import math

#coeffecients
a=3
b=-1
c=-4
#writing the equation
x = np.linspace(-4,4,100)
p=np.poly1d([a,b,c])
for i in range(len(x)):
    y=p(x)

#zeroes
#s=math.sqrt(b**2-4*a*c)
#k1=(-1*b+s)/(2*a)
#k2=(-1*b-s)/(2*a)
roots=p.r

A=np.array([roots[0],0])
B=np.array([roots[1],0])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.001), A[1] * (1 - 0.01) , 'k1')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.005), B[1] * (1-0.01) , 'k2')
plt.plot(x,y,label='$p(x)=3x^2-x-4$')
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')
plt.savefig('./pyfigs/conic2d.eps')
plt.show() 
