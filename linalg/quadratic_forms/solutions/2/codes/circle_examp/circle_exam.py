import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#vertices
A = np.array([[1, 0], [0, 1]])
B = np.array([8, 10])
C = -8
O = findingOandr(A, B, C)[0]
r = findingOandr(A, B, C)[1]
D = O + np.array([r, 0])
print(findingOandr(A, B, C))

#plot circle
circle1 = plt.Circle((O[0], O[1]), r, color='b', fill=False)

#Generating all lines
x_OD = line_gen(O, D)

fig, ax = plt.subplots()
ax.grid()

#Plotting all lines
ax.plot(x_OD[0,:], x_OD[1,:], linestyle='dotted')
ax.add_artist(circle1)

ax.text(O[0], O[1] * (1 - 0.2), '$O$')
ax.plot(O[0], O[1], 'o')
ax.text(O[0] * (1 - 0.7), O[1] * (1 - 0.2), '$r$')
ax.plot(O[0], O[1], 'o')

ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim((-15, 5))


# if using termux
# ax.fig('./figs/circle.eps')
# ax.fig('./figs/circle.pdf')
# subprocess.run(shlex.split("termux-open ./figs/circle.pdf"))
# else
fig.savefig('./figs/circle_examp/circle.eps')