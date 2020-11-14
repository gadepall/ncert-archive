import numpy as np

# Taking values  y=1 and k=2 in the given determinant (3.10,18(ii)) and check whether it is 20.
X = np.array([[[3,1,1],[1,3,1],[1,1,3]]])

# Calculating determinant of x
detx = np.linalg.det(X)
print("The value of determinant is = ", detx)
print("\nHence proved.")




