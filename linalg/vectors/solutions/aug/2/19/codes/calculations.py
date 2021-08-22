import numpy as np

A = np.array([4,8,10])
B = np.array([6,10,-8])

# For YZ plane
n = np.array([1,0,0])
d = 0

# ratio 
k = (d-n.T@A)/(n.T@B-d)
print('k =',k)

# point of intersection
P = (A+k*B)/(k+1)
print('P =',P)
