# Let A =(3 1 \\ -1 2). Show that A^2 - 5A + 7I = 0. Hence find A^-1.

import numpy as np
A = np.array([[3,1],[-1,2]])
I = np.array([[1,0],[0,1]])
Sq_A = np.dot(A,A)
Result = Sq_A - 5*A + 7*I
print("The result of A^2 - 5A + 7I = \n", Result)

Inverse = (1/7)*(5*I - A)
print("The Inverse of the matrix is A^-1 = 1/7[5I - A] : \n", Inverse)