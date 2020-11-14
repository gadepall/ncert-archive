import numpy as np
import matplotlib.pyplot as plt
import math

len = 100

I=np.array([2,2])
A=np.array([4,5])
r= math.sqrt((I[0] - A[0])**2 + (I[1] - A[1])**2)  
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + I).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.2) , '(2,2)')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1) , '(4,5)')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
