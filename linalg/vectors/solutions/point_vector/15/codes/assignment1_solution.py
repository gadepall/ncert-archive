import numpy as np

a = [1,4,2]
b = [3, -2, 7]
c = [2, -1, 4]

B = [0, 0, 15]

"""

Representing the 3 equations in the matrix format

 x + 4y + 2z = 0
3x - 2y + 7z = 0
2x -  y + 4z = 15 

"""

A = np.array([a, b, c])

d = np.linalg.solve(A,B)

print(d)

# output is [ 53.33333333  -1.66666667 -23.33333333]




