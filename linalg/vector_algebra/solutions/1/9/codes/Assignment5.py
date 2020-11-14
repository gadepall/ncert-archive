
import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code


#Plotting for showing the graph :

#Inputs
A = np.array([0,0]) #Assuming A as origin
B = np.array([24,0])  # Assuming suitable cordinates of B
P = np.array([12,5]) # Assuming suitable cordinates of P
Q = np.array([12,-9]) #Assuming suitable cordinates of Q
#Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(P,Q)
x_EF = line_gen(A,P)
x_GH = line_gen(B,P)
x_IJ = line_gen(A,Q)
x_KL = line_gen(B,Q)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_EF[0,:],x_EF[1,:])
plt.plot(x_GH[0,:],x_GH[1,:])
plt.plot(x_IJ[0,:],x_IJ[1,:])
plt.plot(x_KL[0,:],x_KL[1,:])


plt.plot(A[0], A[1], 'o')
plt.plot(B[0], B[1], 'o')
plt.plot(P[0], P[1], 'o')
plt.plot(Q[0], Q[1], 'o')
plt.plot(12, 0, 'o')

plt.annotate("A", (0, 0))
plt.annotate("B", (24, 0))
plt.annotate("M", (12, 0))
plt.annotate("P", (12, 5))
plt.annotate("Q", (12, -9))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()


