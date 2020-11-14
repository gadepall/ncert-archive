import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#vertices
A = np.array([10, 0])
B = np.array([-10, 0])
C = np.array([0, 0])
D = np.array([3, 0])

X_coord = np.array(np.linspace(-9.0, 9.0, num=19))
Y_coord = np.zeros(19)

#Generating all lines
x_DB = line_gen(D, B-[np.nextafter(0, 1), 0])
x_AB = line_gen(A, B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], color='black', label='Number line')
plt.plot(x_DB[0,:], x_DB[1,:], label='Values of x which satisfy the inequality')
plt.plot(X_coord, Y_coord, 'o')

plt.plot(A[0], A[1], '>',)
plt.text(A[0], 0.005, '$∞$')
plt.plot(B[0], B[1], '<')
plt.text(B[0], 0.005, '$-∞$')
plt.plot(C[0], C[1], 'o')
plt.text(C[0], 0.005 , '$0$')
plt.plot(D[0], D[1], 'o')
plt.text(D[0], 0.005 , '$3$')

plt.axis('off')
plt.legend(loc='best')
#if using termux
# plt.savefig('./figs/number_line.pdf')
# plt.savefig('./figs/number_line.eps')
# subprocess.run(shlex.split("termux-open ./figs/number_line.pdf"))
#else
plt.show()
