#Code by GVV Sharma
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import*

P= np.array([2,-3])
Q1= np.array([10,3])
Q2= np.array([10,-9])


#Generating all lines
x_PQ1 = line_gen(P,Q1)
x_PQ2 = line_gen(P,Q2)

#Plotting all lines
plt.plot(x_PQ1[0,:],x_PQ1[1,:],label='$PQ$')
plt.plot(x_PQ2[0,:],x_PQ2[1,:],label='$PQ$')


plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(Q1[0], Q1[1], 'o')
plt.text(Q1[0] * (1 - 0.02), Q1[1] * (1-0.3) , 'Q')
plt.plot(Q2[0], Q2[1], 'o')
plt.text(Q2[0] * (1 + 0.01), Q2[1] * (1 - 0.01) , 'Q')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

plt.show()

