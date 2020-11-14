#Code by GVV Sharma
#November 25, 2019
#released under GNU GPL

#This program plots the circumcircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
import subprocess
import shlex
#end if

#Triangle vertices
#A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')
A,B,C=tri_vert(5,6,4)

def tri_vert2(a,b,c):
  p = (a**2 + c**2-b**2 )/(2*a)
  q = np.sqrt(c**2-p**2)
  A = np.array([p,q]) 
  B = np.array([0,0]) 
  C = np.array([a,0]) 
  return  A
  
D=tri_vert2(5,4,6)
E = np.array([C[0],(C[0]/D[0])*D[1]])
len = 100

p = np.zeros(2)

O,r = ccircle(A,B,C)
print(D,E)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

x_DB = line_gen(D,B)
x_DC = line_gen(D,C)

#x_ED = line_gen(E,D)
#x_EC = line_gen(E,C)


theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T

print(A,B,C,O,r)
#Plotting all lines
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')

#plt.plot(x_ED[0,:],x_ED[1,:],'--',label='$DB$')
#plt.plot(x_EC[0,:],x_EC[1,:],'--',label='$DC$')

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 ), D[1] * (1 - 0.1) , 'D')

#plt.plot(E[0], E[1], 'o')
#plt.text(E[0] * (1 ), E[1] * (1 - 0.1) , 'E')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('c_circle.pdf')
plt.savefig('c_circle.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()


