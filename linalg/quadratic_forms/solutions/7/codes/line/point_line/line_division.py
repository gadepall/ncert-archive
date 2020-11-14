#Code by GVV Sharma
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import*

A= np.array([-2,2])
B= np.array([2,8])

D= np.add(B,3*A)/4
E=np.add(2*B,2*A)/4
F=np.add(3*B,A)/4

#Generating all lines
x_AD = line_gen(A,B)
x_DE = line_gen(D,E)
x_EF = line_gen(E,F)
x_FB = line_gen(F,B)

#Plotting all lines
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
plt.plot(x_FB[0,:],x_FB[1,:],label='$FB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 - 0.2), E[1] * (1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()

