import numpy as np

# Get a, b, c
a = int(input())
b = int(input())
c = int(input())

# Format the matrix
matrix = np.array([[1, 1, 1], [a, b, c], [a**3, b**3, c**3]])

# Determinant using built in functions:
det = np.linalg.det(matrix)
print(round(det))

# Determinant using RHS eqn.
det_eqn = (a - b)*(b - c)*(c - a)*(a + b + c)
print(det_eqn)
