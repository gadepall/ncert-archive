import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

P = np.array([-5,-1])
Q = np.array([3,-5])
R = np.array([5,2])

x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)

plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.05), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')

plt.title("Triangle PQR")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()