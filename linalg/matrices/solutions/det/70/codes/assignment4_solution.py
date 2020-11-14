import numpy as np

x = np.cos(np.deg2rad(30))
y = np.sin(np.deg2rad(60))
u = np.sin(np.deg2rad(30))
v = np.cos(np.deg2rad(60))


m1 = np.array([
    [x*y, x*v, -1*u],
    [-1*v, y, 0],
    [u*y, u*v, x]
])

print(np.linalg.det(m1)

'''
Output = 1.0

'''