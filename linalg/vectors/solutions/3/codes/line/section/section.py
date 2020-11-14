import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()


#coodinates of points
A = np.array([-3,10])
B = np.array([6,-8])
C = np.array([-1,6])

#finding ratio
#C={kB+A}/{k+1}
k=np.linalg.norm(A-C)/np.linalg.norm(C-B)
print("ratio in which C divides AB is")
print(k)


#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.03), B[1] * (1 + 0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.03), C[1] * (1 + 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('./pyfigs/section.eps')

plt.show()

