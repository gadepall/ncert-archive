import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#vertices
theta = -60
A = np.array([0, 25])
B = np.array([10 * np.cos(np.pi / 180 * theta), 10 * np.sin(np.pi / 180 * theta)])
O = np.array([0, 0])
C = A + B # resultant
angC = findAngle(O, A, C)
print(A, B, C, np.linalg.norm(C), angC)

#generating lines
x_AO = line_gen(A, O)
x_BO = line_gen(B, O)
x_CO = line_gen(C, O)

#Plotting all lines
plt.plot(x_AO[0,:], x_AO[1,:], label='Velocity of the boat')
plt.plot(x_BO[0,:], x_BO[1,:], label='Water cuurent')
plt.plot(x_CO[0,:], x_CO[1,:], label='Resultant velocity', linestyle='dotted')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.04), A[1] * (1 + 0.02), 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1], 'B')
plt.plot(O[0], O[1], 'o')
plt.text(1, O[1], 'O')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1], 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

# if using termux
# plt.savefig('./figs/motion_plane.pdf')
# plt.savefig('./figs/motion_plane.eps')
# subprocess.run(shlex.split("termux-open ./figs/motion_plane"))
# else
plt.show()
