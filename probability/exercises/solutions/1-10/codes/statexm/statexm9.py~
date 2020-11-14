import numpy as np
import matplotlib.pyplot as plt
import math
#from coeffs import *
import subprocess
import shlex

def line_gen(A,B):
	len = 20
	dim = A.shape[0]
	x_AB = np.zeros((dim,len))
	lam_1 = np.linspace(0,1,len)
	for i in range(len):
		temp1 = A + lam_1[i]*(B-A)
		x_AB[:,i]=temp1.T
	return x_AB

#vertices
A = np.array([5,30])
B= np.array([10,28])
C = np.array([15,16])
D = np.array([20,14])
E = np.array([25,10])
F = np.array([30,7])
G = np.array([35,3])

H = np.array([10,2])
I= np.array([15,14])
J = np.array([20,16])
K = np.array([25,20])
L = np.array([30,23])
M = np.array([35,27])
N = np.array([40,30])

O = np.array([17.5,15])


#Generating the lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DE = line_gen(D,E)
x_EF = line_gen(E,F)
x_FG = line_gen(F,G)

x_HI = line_gen(H,I)
x_IJ= line_gen(I,J)
x_JK = line_gen(J,K)
x_KL = line_gen(K,L)
x_LM = line_gen(L,M)
x_MN = line_gen(M,N)

#plotting the all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DE[0,:],x_DE[1,:])
plt.plot(x_EF[0,:],x_EF[1,:])
plt.plot(x_FG[0,:],x_FG[1,:])

plt.plot(x_HI[0,:],x_HI[1,:])
plt.plot(x_IJ[0,:],x_IJ[1,:])
plt.plot(x_JK[0,:],x_JK[1,:])
plt.plot(x_KL[0,:],x_KL[1,:])
plt.plot(x_LM[0,:],x_LM[1,:])
plt.plot(x_MN[0,:],x_MN[1,:])



plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1), A[1]*(1-0.1), 'A')
plt.plot(B[0],B[1],'o')
plt.plot(C[0],C[1],'o')
plt.plot(D[0],D[1],'o')
plt.plot(E[0],E[1],'o')
plt.plot(F[0],F[1],'o')
plt.plot(G[0],G[1],'o')
plt.text(G[0]*(1), G[1]*(1-0.1), 'G')

plt.plot(H[0],H[1],'o')
plt.text(H[0]*(1), H[1]*(1-0.1), 'H')
plt.plot(I[0],I[1],'o')
plt.plot(J[0],J[1],'o')
plt.plot(K[0],K[1],'o')
plt.plot(L[0],L[1],'o')
plt.plot(M[0],M[1],'o')
plt.plot(N[0],N[1],'o')
plt.text(N[0]*(1), N[1]*(1-0.1), 'N')

plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1), O[1]*(1-0.1), 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('../../figures/statexm/statexm9.eps')

plt.show()
