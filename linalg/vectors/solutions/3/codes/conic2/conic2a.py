import numpy as np
import matplotlib.pyplot as plt
import subprocess
import  shlex
import math

#coeffecients
a=12
b=-7
c=1
#writing the equation
x = np.linspace(-3,3,100)
p=np.poly1d([a,b,c])
for i in range(len(x)):
    y=p(x)

roots=p.r


A=np.array([roots[0],0])
B=np.array([roots[1],0])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'k1')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.5), B[1] * (1-0.1) , 'k2')
plt.plot(x,y,label='$p(x)=12x^2-7x+1$')
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')
plt.savefig('./pyfigs/conic2a.eps')
plt.show() 
