

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if



#Inputs
A=np.array([-1,7])
B=np.array([4,-3])
k=2/3
#Generating all lines
C=(k*A+B)/(k+1)


x_AC = line_gen(A,C)
x_CB = line_gen(C,B)


#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.3), B[1] * (1-0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1-0.3), C[1] * (1-0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#if using termux
#plt.savefig('./line/figs/line_icept.pdf')
#plt.savefig('./line/figs/line_icept.eps')
#subprocess.run(shlex.split("termux-open ./line/figs/line_icept.pdf"))
#else
plt.show()


