from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

xx, yy = np.meshgrid(range(10), range(10))
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

A = np.array([2,-1,1]).reshape((3,1))
B = np.array([1,-3,-5]).reshape((3,1))
C = np.array([3,-4,-4]).reshape((3,1))

S=C-A
print(S)
K=C-B
print(K)
L=B-C
print(L)

Z= np.transpose(B-A)
print(Z)
T=np.transpose(A-B)
print(T)
X=np.transpose(A-C)
print(X)

N=Z@S
print(N)

P=T@K
print(P)

Q= X@L
print(Q)

def line_gen(A,B):
  len =10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)



plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CA[0,:],x_CA[1,:],x_CA[2,:],label="CA")


ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.text(2,-1,1, "A", color='red')
ax.text(1,-3,-5, "B", color='red')
ax.text(3,-4,-4, "C", color='red')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()