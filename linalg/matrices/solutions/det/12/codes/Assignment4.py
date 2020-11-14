import numpy as np

# Taking values a=2, b=3 and c=5 in the given determinant (3.10,12) and check whether it is zero.
X = np.array([[[1,15,16],[1,10,21],[1,6,25]]])

# Calculating determinant of x
detx = np.linalg.det(X)
print("The value of determinant is = ", detx)
print("\nHence proved.")
