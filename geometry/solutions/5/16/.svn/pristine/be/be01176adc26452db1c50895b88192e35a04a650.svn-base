import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

# theta goes from 0 to 2pi
theta = np.linspace(0, 2*np.pi, 100)

# the radius of the circle
r = np.sqrt(4)

# compute x1 and x2
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

# create the figure
fig, ax = plt.subplots(1)
ax.plot(x1, x2,label= '$circle$')
ax.set_aspect(1)

A= np.array([2,0])
B=np.array([-2,0])
C=np.array([1.414,1.414])
D=np.array([-0.518, 1.932])
E=np.array([0.597,3.385])
O=np.array([0,0])

#Generating all lines
x_AB = line_gen(A,B)
x_BD = line_gen(B,D)
x_AC = line_gen(A,C)
x_CD = line_gen(C,D)
x_CE = line_gen(C,E)
x_DE = line_gen(D,E)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_CE[0,:],x_CE[1,:],label='$CE$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$',linestyle ='dashed')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$',linestyle ='dashed')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$',linestyle ='dashed')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$',linestyle ='dashed')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.05), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 + 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.3), E[1] * (1+ 0.01) , 'E')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 - 0.2), O[1] * (1 + 0.3) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
#plt.grid() # minor
plt.axis('equal')

plt.show()
