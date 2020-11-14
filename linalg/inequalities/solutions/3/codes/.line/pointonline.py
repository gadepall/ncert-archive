
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()

#For y1 and c1
#4x+3y=12 
#x1 = np.array([xA,yA])
D1 = np.array([12,0])
M1 = np.array([[4,3],[1,0]])
M1inv=np.linalg.inv(M1)
y1=M1inv@D1
c1=y1+np.array([3,-4])
#For y2 and c2
#2x+5y=0
#y2 = np.array([xA,yA])
D2 = np.array([0,0])
M2 = np.array([[2,5],[1,0]])
M2inv=np.linalg.inv(M2)
y2=M2inv@D2
c2=y2+np.array([5,-2])
#For y1 and c1
#3y=4 
#11 = np.array([xA,yA])
D3 = np.array([4,0])
M3 = np.array([[0,3],[1,0]])
M3inv=np.linalg.inv(M1)
y3=M3inv@D3
c3=y3+np.array([3,0])

#plotting points
plt.plot(y1[0], y1[1], 'o')
plt.text(y1[0] * (1 - 0.1), y1[1] * (1 + 0.1) , 'y1')
plt.plot(y2[0], y2[1], 'o')
plt.text(y2[0] * (1 - 0.1), y2[1] * (1 + 0.1) , 'y2')
plt.plot(y3[0], y3[1], 'o')
plt.text(y3[0] * (1 - 0.1), y3[1] * (1 + 0.1) , 'y3')
plt.plot(c1[0], c1[1], 'o')
plt.text(c1[0] * (1 - 0.1), c1[1] * (1 + 0.1) , 'c1')
plt.plot(c2[0], c2[1], 'o')
plt.text(c2[0] * (1 - 0.1), c2[1] * (1 + 0.1) , 'c2')
plt.plot(c3[0], c3[1], 'o')
plt.text(c3[0] * (1 - 0.1), c3[1] * (1 + 0.1) , 'c3')

#plotting the lines
x=np.linspace(-10,10,500)
y1=(-4*x+12)/3
plt.plot(x,y1,label='4x+3y=12')
y2=-2*x/5
plt.plot(x,y2,label='2x+5y=0')
y3=4/3+0*x
plt.plot(x,y3,label='3y=4')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

plt.savefig('./pyfigs/pointonline.eps')

#print(3)
plt.show()
#print(4)



