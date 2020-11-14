import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#vertices
A = np.array([0, 0])
B = np.array([36, 15])

length = np.linalg.norm(dir_vec(A, B))
print(length)

#generating lines
x_AB = line_gen(A, B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(A[0], A[1], 'o')
plt.text(-1, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.04), B[1], 'B')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

# if using termux
# plt.savefig('./figs/dist_bt_pts.pdf')
plt.savefig('./figs/dist_bt_pts.eps')
# subprocess.run(shlex.split("termux-open ./figs/dist_bt_pts"))
# else
# plt.show()
