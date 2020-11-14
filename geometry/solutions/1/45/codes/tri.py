import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *

#Assuming the sides of the triangle with PR > PQ

p = 6
q = 5
r = 4

#Coordinates of P 
a = (p**2 + r**2-q**2 )/(2*p)
b = np.sqrt(r**2-a**2)

#Point S is found using Triangle Angle Bisector Theorem.
#According to it, QS/PQ = SR/PR from which QS(=x) turns out to be 8/3
x=8/3

#Triangle vertices
P = np.array([a,b]) 
Q = np.array([0,0]) 
R = np.array([p,0])
S = np.array([x,0])
print(P[0],P[1])
#Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)
x_PS = line_gen(P,S)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_PS[0,:],x_PS[1,:],label='$PS$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1.2), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0]+0.2, Q[1]+0.2 , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')
plt.plot(S[0],S[1],'o')
plt.text(S[0]*(1.05),S[1]+0.2,'S')

print(P[0],P[1])
print(Q[0],Q[1])
print(R[0],R[1])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()