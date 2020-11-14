import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

#From the information given 
#solving the equations:
# 4y-4x=160
# 3y-7x=180
# x = -15
# y = 25
# angA = 120
# angB = 70
# angC = 60
# angD = 110

#From the information given 
p = np.array([[-4, 4], [-7, 3]])
q = np.array([160, 180])
result = np.linalg.inv(p).dot(q)
print(result)

angA = 4 * result[1] + 20
angB = 3 * result[1] - 5
angC = -4 * result[0] 
angD = -7 * result[0] + 5

#sides
a = 10
b = 8

#Quad vertices
A = np.array([0, 0])
B = np.array([a, 0])
D = np.array([b * np.cos(angA * np.pi / 180), b * np.sin(angA * np.pi / 180)])
C = findingTheThirdCoord(np.linalg.norm(A-B) , 180-angB-findAngle(D, A, B), angB)
print(A, B, C, D)


#Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CD = line_gen(C, D)
x_DA = line_gen(D, A)
x_CA = line_gen(C, A)
x_DB = line_gen(D, B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CD[0,:], x_CD[1,:], label='$CD$')
plt.plot(x_DA[0,:], x_DA[1,:], label='$DA$')
plt.plot(x_CA[0,:], x_CA[1,:], linestyle='dotted', label='$CA$')
plt.plot(x_DB[0,:], x_DB[1,:], linestyle='dotted', label='$DB$')

plt.plot(A[0], A[1], 'o')
plt.text(-1, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.04), B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 + 0.015) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.07), D[1] * (1 + 0.08) , 'D')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

# if using termux
# plt.savefig('./figs/cyclic_quad.pdf')
# plt.savefig('./figs/cyclic_quad.eps')
# subprocess.run(shlex.split("termux-open ./figs/cyclic_quad.pdf"))
# else
plt.show()
