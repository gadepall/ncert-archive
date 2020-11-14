import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

#input params
b = 5 # baselength
h = 3 #altitude
angA = 70 #angle made by the base and one side

temp_vec = np.array([h / np.tan(np.pi / 180 * angA), 0])
height_vec = np.array([0, h])

#Quad vertices
A = np.array([0, 0])
B =  A + np.array([b, 0])
C = B - temp_vec + height_vec
D = A + temp_vec + height_vec
O = circumCenter(A, B, C)
#foot of perpendicular
P1 = A + temp_vec
P2 = B - temp_vec

print(A, D, B, C, O)
print(P1,P2)
print(np.linalg.norm(A-O))

#Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_DC = line_gen(D, C)
x_AD = line_gen(A, D)
x_DP1 =  line_gen(D, P1)
x_CP2 =  line_gen(C, P2)
circle1 = plt.Circle((O[0], O[1]), np.linalg.norm(A-O), color='b', fill=False, linestyle='dotted')

fig, ax = plt.subplots()

#Plotting all lines
ax.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
ax.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
ax.plot(x_DC[0,:], x_DC[1,:], label='$DC$')
ax.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
ax.add_artist(circle1)
#for perpendicular
# plt.plot(x_DP1[0,:], x_DP1[1,:], linestyle='dotted', label='$DP1$')
# plt.plot(x_CP2[0,:], x_CP2[1,:], linestyle='dotted', label='$CP2$')

ax.plot(A[0], A[1], 'o')
ax.text(-0.5, 0.05, 'A')
ax.plot(B[0], B[1], 'o')
ax.text(B[0] * (1 + 0.04), B[1], 'B')
ax.plot(C[0], C[1], 'o')
ax.text(C[0] * (1 + 0.05), C[1] * (1 + 0.05) , 'C')
ax.plot(D[0], D[1], 'o')
ax.text(D[0] * (1 - 0.6), D[1] * (1 + 0.05) , 'D')
ax.plot(O[0], O[1], 'o')
ax.text(O[0] * (1 - 0.1), O[1] * (1 + 0.8) , 'O')
#labelling the foot of perpendicular
# plt.plot(P1[0], P1[1], 'o')
# plt.text(P1[0] * (1 + 0.03), -0.4 , 'P1')
# plt.plot(P2[0], P2[1], 'o')
# plt.text(P2[0] * (1 + 0.03), -0.4 , 'P2')

ax.set_xlim((-5, 10))
ax.set_ylim((-5, 5))
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='best')
ax.set_aspect('equal', adjustable='datalim')
ax.grid()

#if using termux
# fig.savefig('./figs/trapezium.eps')
# fig.savefig('./figs/trapezium.eps')
# subprocess.run(shlex.split("termux-open ./figs/trapezium.eps"))
# else
# fig.savefig('./figs/trapezium.eps')