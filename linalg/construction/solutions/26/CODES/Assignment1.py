import numpy as np
import matplotlib.pyplot as plt


#Sides
CA = 6
BC = 6

#Calculating third side 
AB=((CA*CA)+(BC*BC))**(0.5)

#Triangle vertices
A = np.array([0,CA]) 
C = np.array([0,0]) 
B = np.array([BC,0]) 


#Generating all lines
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.savefig('github/ncert/linalg/construction/solutions/26/CODES/test.png')
plt.grid() # minor
