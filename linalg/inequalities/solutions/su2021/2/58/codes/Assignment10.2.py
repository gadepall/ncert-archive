import numpy as np
import matplotlib.pyplot as plt

#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
  return P

#Line Parameters
n1 = np.array([1,2])
n2 = np.array([1,1])
n3 = np.array([-1,1])
n4 = np.array([-1,0])

c1 = 10
c2 = 1
c3 = 0
c4 = 0


#Intersection of the lines
A=line_intersect(n1,c1,n4,c4)
B=line_intersect(n1,c1,n3,c3)
C=line_intersect(n2,c2,n3,c3)
D=line_intersect(n2,c2,n4,c4)
points = np.array((A,B,C,D))

#Filling up the desired region
plt.fill(points[:,0], points[:,1], 'gray', alpha=0.4)

#Plotting points of Intersection
plt.plot(A[0], A[1], 'o')
plt.text(A[0]+0.05, A[1] * (1 ) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1+0.004 ), B[1] * (1)-0.02 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.2) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.2) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid() # minor

plt.show()
