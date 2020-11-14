import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

#Sides
ac = 5
ad = 5
lamda = 6

#Angles
angA = 80

#Quad vertices
A = np.array([0, 0])
C = np.array([ac, 0])
D = np.array([ad * np.cos(np.pi / 180 * angA), ad * np.sin(np.pi / 180 * angA)])
B = A + angleBisector(A, C, D) * lamda
O = np.array(inncenter(A,D,C))
P1 = np.array(alt_foot(O,A,C))
P2 = np.array(alt_foot(O,A,D))
print(A, C, B, D, O, P1, P2)


#Generating all lines
x_AC = line_gen(A, C)
x_AD = line_gen(A, D)
x_DB = line_gen(D, B)
x_BC = line_gen(B, C)
x_AB = line_gen(A, B)
x_OP1 = line_gen(O, P1)
x_OP2 = line_gen(O, P2)
x_P1P2 = line_gen(P1, P2)


#Plotting all lines
plt.plot(x_AC[0,:], x_AC[1,:], label='$AC$')
plt.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
plt.plot(x_DB[0,:], x_DB[1,:], label='$DB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_AB[0,:], x_AB[1,:], linestyle='dashed', label='$AB$')
plt.plot(x_OP1[0,:], x_OP1[1,:], linestyle='dashed', label='$OP1$')
plt.plot(x_OP2[0,:], x_OP2[1,:], linestyle='dashed', label='$OP2$')
plt.plot(x_P1P2[0,:], x_P1P2[1,:], linestyle='dashed', label='$P1P2$')

plt.plot(O[0], O[1],'o')
plt.text(O[0] * (1 + 0.1), O[1], 'O')
plt.plot(P1[0], P1[1],'o')
plt.text(P1[0], -0.3, 'P1')
plt.plot(P2[0], P2[1],'o')
plt.text(P2[0] * (1 - 1.5) , P2[1], 'P2')
plt.plot(A[0], A[1], 'o')
plt.text(0.3, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.02), B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.2), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

#if using termux
# plt.savefig('./figs/quad.pdf')
# plt.savefig('./figs/quad.eps')
# subprocess.run(shlex.split("termux-open ./figs/quad.pdf"))
#else
plt.show()