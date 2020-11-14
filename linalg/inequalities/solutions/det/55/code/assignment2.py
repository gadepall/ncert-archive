import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = int(input())
# Defining input
eq_1 = np.array([[1, 1, 1]])
eq_2 = np.array([[2, 3, 2]])
eq_3 = np.array([[1, 1, 2]])
eq_3 = a * eq_3

A = np.concatenate((eq_1, eq_2, eq_3), axis = 0)
B = np.array([[1, 2, 4]])
B1 = np.array([1, 2, 4]) # copy of B for solving purposes
# Check if the system is consistent
A_aug_B = np.concatenate((A, B), axis = 0)
# A[2, 2]
(m, n) = np.shape(A) # Dimension of the matrix
rank_A = np.linalg.matrix_rank(A)
rank_A_aug_B = np.linalg.matrix_rank(A_aug_B)
if(rank_A == rank_A_aug_B):
  if(rank_A == n):
    print("The system is consistent")
  else:
    print("System consistent, has infinite solutions")
else:
  print("The system might be inconsistent")

# Solving the equation
solution = np.linalg.solve(A, B1)
print(solution)

#Plotting the solution
fig = plt.figure().gca(projection='3d')
#ax = fig.add_subplot(111, projection='3d')
X_val = np.arange(-10, 10, 5)
Y_val = np.arange(-10, 10, 5)
X, Y = np.meshgrid(X_val, Y_val)
z_1 = 1 - (X + Y)
z_2 = (2 - (2*X + 3*Y))/2
z_3 = (4 - (X + Y))/2

# Setting up the plot

#fig.plot_surface(X, Y, z_1, color = "yellow", alpha = 0.3)
#fig.plot_surface(X, Y, z_2, color = "red", alpha = 0.3)
#fig.plot_surface(X, Y, z_3, color = "blue", alpha = 0.2)
#fig.plot([solution[0]], [solution[1]], [solution[2]], markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5, alpha=0.6)
#fig.set_xlabel('x', color='blue')
#fig.set_ylabel('y', color='blue')
#fig.set_zlabel('z', color='blue')
#yellow_proxy = plt.Rectangle((0, 0), 1, 1, fc='y', alpha = 0.3)
#red_proxy = plt.Rectangle((0, 0), 1, 1, fc='r', alpha = 0.3)
#blue_proxy = plt.Rectangle((0, 0), 1, 1, fc='b', alpha = 0.2)
#black_proxy = plt.Line2D([0], [0], linestyle="none", marker='o', alpha=0.6, markersize=10, markerfacecolor='black')
#fig.legend([yellow_proxy,red_proxy, blue_proxy, black_proxy], [r'$x+y-z=1$',r'$x-y+z=1$', r'$-x+y+z=1$', r'$Sol.\; (1,1,1)$'], numpoints=1, loc='upper left')
#fig.set_title(r'$Graphical\; Representation\; of\; the\; System\;$', fontsize=18)
#plt.show()