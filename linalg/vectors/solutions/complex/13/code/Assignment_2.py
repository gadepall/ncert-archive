import numpy as np
import matplotlib.pyplot as plt

import math
import cmath
#z1 = 2-i
r1= 2
i1= -1
#z2 = -2+i
r2 = -2
i2 = 1
D1 = np.array([1,0])
z1 = np.array([[r1,-i1],[i1,r1]])
z2 = np.array([[r2,-i2],[i2,r2]])
z1_conjugate =  np.array([[r1,i1],[-i1,r1]])
z1_conjugate_inv=np.linalg.inv(z1_conjugate)
equation_a=np.matmul(z1,np.matmul(z2,np.matmul(z1_conjugate_inv,D1)))
print("The required complex number in equation a is",equation_a)
print("Real part of equation a is:",equation_a[0])
b=np.matmul(z1,z1_conjugate)
equation_b=np.matmul(np.linalg.inv(b),D1)
print("The required complex number in equation b is",equation_b)
print("Imaginary part of equation b is:",equation_b[1])
