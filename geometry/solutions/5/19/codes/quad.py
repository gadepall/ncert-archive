import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from quad1 import *
#A = np.array([3,4])
#B = np.array([0,0])
#C = np.array([9,0])
#D = np.array([7,6])

R1=ang_bis(A,B,C)
n1 = np.matmul(omat,R1)
R2=ang_bis(D,C,B)
n2 = np.matmul(omat,R2)
E = line_intersect(n1,B,n2,C)
R3=ang_bis(D,A,B)
n3=np.matmul(omat,R3)
R4=ang_bis(A,D,C)
n4=np.matmul(omat,R4)
G=line_intersect(n3,A,n4,D)
F=line_intersect(n1,B,n3,A)
H=line_intersect(n4,D,n2,C)

print(E,F,G,H)
a=np.linalg.norm(dir_vec(E,F))
b=np.linalg.norm(dir_vec(F,G))
c=np.linalg.norm(dir_vec(E,G))


len=100
O = tri_ccentre(E,F,G)
R = tri_cradius(a,b,c)
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = R*np.cos(theta)
x_circ[1,:] = R*np.sin(theta)
x_circ = (x_circ.T + O).T


#drawing lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)
x_CD = line_gen(C,D)
x_BE = line_gen(B,E)
x_CE = line_gen(C,E)
x_AG = line_gen(A,G)
x_DG = line_gen(D,G)

#plt.plot(x_circ[0,:],x_circ[1,:],label='$incircle$')

#plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CE[0,:],x_CE[1,:],label='$CE$')
plt.plot(x_AG[0,:],x_AG[1,:],label='$AG$')
plt.plot(x_DG[0,:],x_DG[1,:],label='$DG$')

plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')



plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
plt.plot(G[0], G[1], 'o')
plt.text(G[0] * (1 + 0.03), G[1] * (1 - 0.1) , 'G')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
plt.plot(H[0], H[1], 'o')
plt.text(H[0] * (1 + 0.03), H[1] * (1 - 0.1) , 'H')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/quad/pgm_sas.pdf')
#plt.savefig('./figs/quad/pgm_sas.eps')subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sas.pdf"))
#else
plt.show()
