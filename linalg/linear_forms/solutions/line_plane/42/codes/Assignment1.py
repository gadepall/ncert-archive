import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code



#finding solution of two linear equation, this will give the foot of the perpendicular
A = np.array([[3, -4], [4, 3]])
B = np.array([[16], [5]])
print(np.linalg.inv(A) @ B)  #this line prints the solution which is the foot of the perpendicular, the same values are used in variable P

#Plotting for showing the graph :

#Inputs
M = np.array([0,-4]) #a point satisfying equation of given line
N = np.array([8,2])  # another point satisfying equation of given line
O = np.array([-1,3])  #given point
P = np.array([68/25,-49/25]) #foot of the perpendicular drawn from given point to the given line (this point is found by solving the problem)

#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')

plt.plot(M[0], M[1], 'o')
plt.plot(N[0], N[1], 'o')
plt.plot(O[0], O[1], 'o')
plt.plot(P[0], P[1], 'o')

plt.annotate("Desired Point (2.72, -1.96)", (P[0], P[1]))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
