import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex
import math
#centre and radius of the circle1
O1=np.array([0,2])
r1=2
#centre and radius of the circle
O2=np.array([-2,32])
r2=4

O3=np.array([1/2,1/4])
r3=1/12

O4=np.array([1,1])
r4=math.sqrt(2)
#parameters
a=5
b=4
#centre and radius of the circle
O5=np.array([-a,-b])
r5=math.sqrt(a**2-b**2)

#point on the circle1
A1=np.array([O1[0]+r1,O1[1]])
#point on the circle
A2=np.array([O2[0]+r2,O2[1]])
A3=np.array([O3[0]+r3,O3[1]])
A4=np.array([O4[0]+r4,O4[1]])
A5=np.array([O5[0]+r5,O5[1]])

#Generating all lines
x_OA1 = line_gen(O1,A1)
x_OA2 = line_gen(O2,A2)
x_OA3 = line_gen(O3,A3)
x_OA4 = line_gen(O4,A4)
x_OA5 = line_gen(O5,A5)

#Plotting all lines
plt.plot(x_OA1[0,:],x_OA1[1,:],label='$r=2$')
plt.plot(x_OA2[0,:],x_OA2[1,:],label='$r=4$')


#plotting circle
len=100
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O1).T
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle(a)$')

x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + O2).T
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle(b)$')

plt.plot(x_OA3[0,:],x_OA3[1,:],label='$r=1/12$')
x_circ3 = np.zeros((2,len))
x_circ3[0,:] = r3*np.cos(theta)
x_circ3[1,:] = r3*np.sin(theta)
x_circ3 = (x_circ3.T + O3).T
plt.plot(x_circ3[0,:],x_circ3[1,:],label='$circle(c)$')


plt.plot(x_OA4[0,:],x_OA4[1,:],label='$r=r^-0.5$')
x_circ4 = np.zeros((2,len))
x_circ4[0,:] = r4*np.cos(theta)
x_circ4[1,:] = r4*np.sin(theta)
x_circ4 = (x_circ4.T + O4).T
plt.plot(x_circ4[0,:],x_circ4[1,:],label='$circle(d)$')


plt.plot(x_OA5[0,:],x_OA5[1,:],label='$r=3$')
x_circ5 = np.zeros((2,len))
x_circ5[0,:] = r5*np.cos(theta)
x_circ5[1,:] = r5*np.sin(theta)
x_circ5 = (x_circ5.T + O5).T
plt.plot(x_circ5[0,:],x_circ5[1,:],label='$circle(e)$')

#plotting points
plt.plot(O1[0], O1[1], 'o')
plt.text(O1[0] * (1 + 0.001), O1[1] * (1 - 0.001) , 'O1')

plt.plot(O2[0], O2[1], 'o')
plt.text(O2[0] * (1 + 0.001), O2[1] * (1 - 0.001) , 'O2')
 
plt.plot(O3[0], O3[1], 'o')
plt.text(O3[0] * (1 + 0.001), O3[1] * (1 - 0.001) , 'O3')

plt.plot(O4[0], O4[1], 'o')
plt.text(O4[0] * (1 + 0.001), O4[1] * (1 - 0.001) , 'O4')

plt.plot(O5[0], O5[1], 'o')
plt.text(O5[0] * (1 + 0.001), O5[1] * (1 - 0.001) , 'O5')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.savefig('./pyfigs/circle2.eps')
plt.show()


