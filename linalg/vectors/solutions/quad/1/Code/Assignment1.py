from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Vertices of 3D triangle
A = np.array([-1,-1,0]).reshape((3,1))
B = np.array([-1,4,0]).reshape((3,1))
C = np.array([5,4,0]).reshape((3,1))
D = np.array([5,-1,0]).reshape((3,1))
P=(A+B)/2
Q=(B+C)/2
R=(C+D)/2
S=(D+A)/2
print("P=",P)
print("Q=",Q)
print("R=",R)
print("S=",S)
#Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)
x_PS = line_gen(P,S)


#plotting line
plt.plot(x_PQ[0,:],x_PQ[1,:],x_PQ[2,:],label="PQ")
plt.plot(x_QR[0,:],x_QR[1,:],x_QR[2,:],label="QR")
plt.plot(x_RS[0,:],x_RS[1,:],x_RS[2,:],label="RS")
plt.plot(x_PS[0,:],x_PS[1,:],x_PS[2,:],label="PS")

#plotting point
ax.scatter(P[0],P[1],P[2],'o')
ax.scatter(Q[0],Q[1],Q[2],'o')
ax.scatter(R[0],R[1],R[2],'o')
ax.scatter(S[0],S[1],S[2],'o')
ax.text(1,2,3, "P", color='red')
ax.text(-1,-2,-1, "Q", color='red')
ax.text(2,3,2, "R", color='red')
ax.text(4,7,6, "S", color='red')


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CD[0,:],x_CD[1,:],x_CD[2,:],label="CD")
plt.plot(x_AD[0,:],x_AD[1,:],x_AD[2,:],label="AD")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(D[0],D[1],D[2],'o')
ax.text(1,2,3, "A", color='red')
ax.text(-1,-2,-1, "B", color='red')
ax.text(2,3,2, "C", color='red')
ax.text(4,7,6, "D", color='red')


#Checking the Quadrilateral PQRS is parallelogram or not

diagonal_bisect1=((P+R)/2)
diagonal_bisect2=((Q+S)/2)
print("diagonal_bisect1=",diagonal_bisect1)
print("diagonal_bisect2=",diagonal_bisect2)
# if diagonal_bisect1[][] and diagonal_bisect2[][] are identical 
# otherwise returns 0
N=1
def areSame(diagonal_bisect1,diagonal_bisect2): 
      
    for i in range(N): 
        for j in range(N): 
            if (diagonal_bisect1[i][j] != diagonal_bisect2[i][j]): 
                return 0
    return 1
  
if (areSame(diagonal_bisect1, diagonal_bisect2)==1): 
    print("Quad PQRS is a parllelogram") 
else: 
    print("Quad PQRS is not a parllelogram")
print("(P-R).T@(Q-S)=",(P-R).T@(Q-S))

print("PQ",np.linalg.norm(P-Q))
print("PS",np.linalg.norm(P-S))
#Testing Rhombus or not
#(If adjacent sides of a parallelogram are equal then it is a Rhombus)
if (P-R).T@(Q-S)==0 :
    print("Quad PQRS is a Rhombus")
else:
    print("Quad PQRS is not a Rhombus")

print("(P-Q).T@(P-S)=",(P-Q).T@(P-S))
#Testing Square or not
#(If adjacent sides of parallelogram are equal and orthogonal to each other then it is a Square)
if ((P-Q).T@(P-S))==0 and (np.linalg.norm(P-Q))==(np.linalg.norm(P-S)):
    print("Quad PQRS is a Square")
else:
    print("Quad PQRS is not a Square")



#Testing Rectangle or not
#(If pythagoras theorem valid on two adjacent sides and diagonal of a parallelogram then it is rectangle)
if ((P-Q).T@(P-S))==0:
    print("Quad PQRS is a Rectangle")
else:
    print("Quad PQRS is not a Rectangle")







#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#plt.savefig('./triangle/figs/quad_3d.pdf')
#plt.savefig('./triangle/figs/quad_3d.eps')
#subprocess.run(shlex.split("termux-open ./triangle/figs/quad_3d.pdf"))
#else
plt.show()
