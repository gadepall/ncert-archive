
#Prob  47 of exercise 8.1
#code by Krishnaja Kodali
#proof that a line parallel to parallel sides of a trap  divides the non parallel sides in equal ratio
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#using termux
import subprocess
import  shlex
#def destroy(self):
	#self.close_event()


#sides of trapezium
a = 4
c = 9
xA = 4
h = 3

# AD/ED=k+1
k = 1

#Coordinates of A
yA = h
#print("coordinates of pt A are "+ str(xA) )

#coordinates of B
xB = xA+a
yB = h

#Trapezium vertices
D = np.array([0,0])
C = np.array([c,0])
A = np.array([xA,yA])
B = np.array([xB,yB])


#finding E by section formulae
E = (k*D + A)/(k+1)
#print(A[1])
#print(B[1])
#If F divides BC in ratio m:1
# F= (m*C + B) / (m+1)
#but E[1] = F[1] as EF is parallel to xaxis
#E[1] = A[1] / (k+1) and F[1]= ((m*C[1])* B[1]) / (m+1)
#equating the above 2 equations we get

m = (A[1]-((k+1)*B[1]))/(((k+1)*C[1])-A[1])

F= (m*C + B) / (m+1)


#other points
#X = np.array([xA,0])
#Y = np.array([xB,0])
#M = np.array([xA,E[1]])
#N = np.array([xB,F[1]])



#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_EF = line_gen(E,F)
#x_AX = line_gen(A,X)
#x_BY = line_gen(B,Y)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
#plt.plot(x_AX[0,:],x_AX[1,:],label='$AX$')
#plt.plot(x_BY[0,:],x_BY[1,:],label='$BY$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.03), B[1] * (1 + 0.1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.02), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.13), D[1] * (1 - 0.13) , 'D')
#print(1)
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 -0.1), E[1] * (1 + 0.03) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 + 0.03) , 'F')
#plt.plot(X[0], X[1], 'o')
#plt.text(X[0] * (1 + 0.03 ), X[1] * (1 - 0.1) , 'X')
#plt.plot(Y[0], Y[1], 'o')
#plt.text(Y[0] * (1 + 0.01), Y[1] * (1 - 0.1) , 'Y')
#plt.plot(M[0], M[1], 'o')
#plt.text(M[0] * (1 + 0.05), M[1] * (1 - 0.1) , 'M')
#plt.plot(N[0], N[1], 'o')
#plt.text(N[0] * (1 - 0.05), N[1] * (1 - 0.1) , 'N')
#print(2)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('./pyfigs/pyfigs.eps')

#print(3)
plt.show()
#print(4)

if (k==m):
	print("AE/ED = BF/FC")
else:
	print("AE/ED != BF/FC")


#print(5)

#generating eps file
#plt.savefig('./figs/prob.pdf')
#subprocess.run(shlex.split("termux-open ./figs/prob.pdf"))



