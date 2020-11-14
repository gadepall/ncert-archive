import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#Quad vertices
A = np.array([6, -6])
B = np.array([3, -7])
C = np.array([3, 3])

p = np.array([[3, 1], [1, -3]])
q = np.array([7, 9])
O = np.sum(np.linalg.inv(p)*q , axis=1)
print(A, B, C, O)

#plot circle
circle1 = plt.Circle((O[0], O[1]), np.linalg.norm(A-O), color='b', fill=False)

fig, ax = plt.subplots()
ax.grid()
ax.add_artist(circle1)
ax.set_aspect('equal', adjustable='datalim')


#plot points and lines
ax.text(A[0], A[1] * (1 - 0.1), 'A')
ax.plot(A[0], A[1] , 'o')
ax.text(B[0], B[1] * (1 - 0.1), 'B')
ax.plot(B[0], B[1], 'o')
ax.text(C[0], C[1] * (1 + 0.1), 'C')
ax.plot(C[0], C[1], 'o')
ax.text(O[0], O[1] * (1 - 0.2), 'O')
ax.plot(O[0], O[1], 'o')


# if using termux
# ax.fig('./figs/circumcircle.eps')
# ax.fig('./figs/circumcircle.pdf')
# subprocess.run(shlex.split("termux-open ./figs/circumcircle.pdf"))
# else
fig.savefig('./circumcircle.png')