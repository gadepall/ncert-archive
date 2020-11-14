import numpy as np

A = np.array([[1, 1],[1, 0]])
B = np.array([[24],[9]])




print(np.dot(np.linalg.inv(A),B))

