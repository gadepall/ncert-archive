import numpy as np
Q = np.array([[0.6, 0.8], [-0.8, 0.6]])
R = np.array([[5, -0.2], [0, 1.4]])
result = Q@R
print(result)