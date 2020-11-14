
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-5,10,100)
y = (x/3) - 11/3

plt.plot(x, y, '-r', label='y=(x-3)/11')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
P= np.array([2,3])
Q=np.array([-1,1])

len = 100

O=np.array([7/2,-5/2])
r=np.linalg.norm(O-P)
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')




plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 + 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.3), Q[1] * (1+ 0.01) , 'Q')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 - 0.2), O[1] * (1 + 0.3) , 'O')


plt.show()
