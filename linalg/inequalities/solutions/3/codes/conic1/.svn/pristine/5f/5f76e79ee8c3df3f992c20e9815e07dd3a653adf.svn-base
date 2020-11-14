import numpy as np
import matplotlib.pyplot as plt
import subprocess
import  shlex
x = np.linspace(-1,1,100)
p=np.poly1d([1,0,-1])
for i in range(len(x)):
    y=p(x)
    
A=np.array([0,p(0)])
B=np.array([1,p(1)])
C=np.array([2,p(2)])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'p(0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.5), B[1] * (1-0.1) , 'p(1)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1-0.5), C[1] * (1-0.1) , 'p(2)')
plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('./pyfigs/conic1b.eps')
plt.show() 
