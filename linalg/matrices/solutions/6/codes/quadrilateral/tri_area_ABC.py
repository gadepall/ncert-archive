import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A = np.array([-4,2])
B = np.array([-3,-5])
C = np.array([3,-2])

area = (1/2)*np.linalg.norm(np.cross(B-A,C-A))

print("Area of triangle ABC: ",area)