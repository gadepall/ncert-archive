import numpy as np

a = np.array([3,2,2])
b = np.array([1,2,-2])

# let A=a+b
A = np.add(a,b)

# let B=a-b
B = np.subtract(a,b)

# a vector C perpendicular to each vectors A and B
# can be found by their cross product
# C = A*B

n = np.cross(A,B)

# unit vector of n is as follows
# np.linalg.norm(n) gives the magnitude of n

unit_vec_n=n/np.linalg.norm(n)
print(unit_vec_n)
