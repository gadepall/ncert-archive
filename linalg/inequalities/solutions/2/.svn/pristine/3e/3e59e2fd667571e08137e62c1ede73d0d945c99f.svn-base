import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

# angA = 20
# angB = 40
# angC = 120

#From the information given 
p = np.array([[6, 0, -1], [0, 3, -1], [1, 1, 1]])
q = np.array([0, 0, 180])
result = np.linalg.inv(p).dot(q)

angA, angB, angC = result

print(result)

# #sides
a = 10

#Quad vertices
A = np.array([0, 0])
B = np.array([a, 0])
C = findingTheThirdCoord(a, angA, angB)
print(A, B, C)


#Generating all lines
x_AB = line_gen(A, B)
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)


#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_AC[0,:], x_AC[1,:], label='$AC$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')

plt.plot(A[0], A[1], 'o')
plt.text(-0.3, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.02), B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 + 0.05) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

#if using termux
# plt.savefig('./figs/triangle_linearalg.pdf')
# plt.savefig('./figs/triangle_linearalg.eps')
# subprocess.run(shlex.split("termux-open ./figs/triangle_linearalg.pdf"))
#else
plt.show()
