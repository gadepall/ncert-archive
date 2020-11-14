#Code by GVV Sharma
#March 6, 2019
#released under GNU GPL

#This program plots the incircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt

len = 100

I=np.array([-3,2])
r=4
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + I).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$incircle$')

plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'O')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

