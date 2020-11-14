#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs10 import *
def pgm(A,B,C,D):
    X = A-B
    Y = D-C
    W = A-D
    Z = B-C

    return ((X.all()==Y.all())and(W.all()==Z.all()))
#if using termux
import subprocess
import shlex
#end if

import numpy as np
S =np.array([[0.5,0],[0,0.5]])
#X =np.array([[x],[y]])
B =np.array([[3],[1.5]])
X = np.linalg.inv(S)@B
print("Values of x and y found are",X[0]," and ",X[1])
x=int(X[0])
y=int(X[1])

A = np.array([1,2])
B = np.array([4,y])
C = np.array([x,6])
D = np.array([3,5])
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],label="BC")
plt.plot(x_CD[0,:],x_CD[1,:],label="CD")
plt.plot(x_AD[0,:],x_AD[1,:],label="AD")

#plotting point
plt.plot(A[0],A[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(C[0],C[1],'o')
plt.plot(D[0],D[1],'o')
plt.text(1,2, "A", color='red')
plt.text(4,3, "B", color='red')
plt.text(6,6, "C", color='red')
plt.text(3,5, "D", color='red')
print("Is this a parallelogram?",pgm(A,B,C,D))
#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
plt.savefig('./figs/q10.pdf')
plt.savefig('./figs/q10.eps')
#subprocess.run(shlex.split("termux-open ./triangle/figs/quad_3d.pdf"))
#else
plt.show()
