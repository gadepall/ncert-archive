import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A = np.array([2,3])
B = np.array([-1,0])
C = np.array([2,-4])

a = np.linalg.norm(B-C)
b = np.linalg.norm(C-A)
c = np.linalg.norm(A-B)

area = (1/2)*np.linalg.norm(np.cross(B-A,C-A))

print("Area of triangle ABC: ",area)