import numpy as np
import matplotlib.pyplot as plt
from coeffss import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
a = 5
b = 6
c = 4

#Triangle vertices
A,B,C = tri_vert(a,b,c)

O = np.array([2,1.5])
l=1
m=1
D = (m*A + l*O)/(l+m)
#print(D)
E = (m*A + l*B)/(l+m)
#print(E)
F = (m*A + l*C)/(l+m)
#print(F)


#D = (A+O)/2
#E = (A+B)/2
#F = (A+C)/2
#randomly chosen point D
print("Is O an interior point?",dotprod(A,B,C,O))
print("Does D lieon AO?",lieonline(A,O,D))
print(A)
print(O)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_DE = line_gen(E,D)
x_DF = line_gen(F,D)
x_EF = line_gen(E,F)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.1), E[1] * (1 - 0.1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.1), F[1] * (1 - 0.1) , 'F')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('similartrianglefig.pdf')
plt.savefig('similartrianglefig.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/tri_ccentre.pdf"))
#else
plt.show()
