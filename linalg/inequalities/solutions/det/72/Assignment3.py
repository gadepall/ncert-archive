import math
import numpy as np

x = 5
a = -3*x                                
matrix = np.array([[x+a,x,x],[x,x+a,x],[x,x,x+a]])
determinant = np.linalg.det(matrix)
print('Determinant of the given matrix when a = -3x is:', determinant)
