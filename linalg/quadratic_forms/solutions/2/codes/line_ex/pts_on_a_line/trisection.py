import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


A = np.array([4, -1])
B = np.array([-2, -3])
C = dividing_line_segment(A, B, 1/2)
D = dividing_line_segment(A, B, 2/1)
print(A, B, C, D)

#Generating all lines
x_AB = line_gen(A, B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.04), A[1] * (1 + 0.04), 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.04), B[1] * (1 + 0.1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 + 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.07), D[1] * (1 + 0.08) , 'D')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

# if using termux
# plt.savefig('./figs/trisection.pdf')
plt.savefig('./figs/trisection.eps')
# subprocess.run(shlex.split("termux-open ./figs/trisection.pdf"))
# else
# plt.show()
