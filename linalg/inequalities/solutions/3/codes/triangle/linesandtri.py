
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()

#For vertex A 
#5x-y=5 and 3x-y=3 
#A = np.array([xA,yA])
D1 = np.array([5,3])
M1 = np.array([[5,-1],[3,-1]])
M1inv=np.linalg.inv(M1)
A=M1inv@D1
print("coordinates of A are ")
print(A)

#For vertex B 
#5x-y=5 and x=0
#B = np.array([xB,yB])
D2 = np.array([5,0])
M2 = np.array([[5,-1],[1,0]])
M2inv=np.linalg.inv(M2)
B=M2inv@D2
print("coordinates of B are ")
print(B)

#For vertex C
#3x-y=3 and x=0
#C = np.array([xC,yC])
D3 = np.array([3,0])
M3 = np.array([[3,-1],[1,0]])
M3inv=np.linalg.inv(M3)
C=M3inv@D3
print("coordinates of C are ")
print(C)


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 +0.1), B[1] * (1 - 0.03) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.02), C[1] * (1 - 0.1) , 'C')
#plotting the lines
x=np.linspace(-1,1,100)
y1=5*x-5
plt.plot(x,y1,label='y=5x-5')
y2=3*x-3
plt.plot(x,y2,label='y=3x-3')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

plt.savefig('./pyfigs/triangle.eps')

#print(3)
plt.show()
#print(4)



