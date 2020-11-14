import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()


#coodinates of towns
A = np.array([0,0])
B = np.array([36,15])
#Finding distance
d=np.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
print(d)
#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.03), B[1] * (1 + 0.1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('./pyfigs/towns.eps')

plt.show()

