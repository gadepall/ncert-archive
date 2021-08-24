import matplotlib.pyplot as plt
import numpy as np

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([5,-2]).reshape((2,1))
B = np.array([6,4]).reshape((2,1))
C = np.array([7,-2]).reshape((2,1))

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

plt.plot(x_AB[0,:],x_AB[1,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],label="BC")
plt.plot(x_CA[0,:],x_CA[1,:],label="CA")

plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1], 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0], B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0], C[1], 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
