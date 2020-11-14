import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

P = np.array([-5,-1])
Q = np.array([3,-5])
R = np.array([5,2])

area = (1/2)*np.linalg.norm(np.cross(Q-P,R-P))

print("Area of triangle PQR: ",area)