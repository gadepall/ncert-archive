import numpy as np
x = int(input("Enter value of x:"))
A = np.array([[x+4, 2*x, 2*x], [2*x, x+4, 2*x], [2*x, 2*x, x+4]])
print("The matrix is as follows:")
print(A)
print("determinant of the matrix is as follows:")
print(np.linalg.det(A))