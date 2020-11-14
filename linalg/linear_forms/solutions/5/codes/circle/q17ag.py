import numpy as np
import matplotlib.pyplot as plt


#Line points
A = np.array([0.707,0.707]) 
B = np.array([0.707,0]) 
C = np.array([1,0]) 
O = np.array([0,0]) 


area1 = 1/2*np.linalg.norm(np.cross(O-B,A-B))
area2 = 1/2*np.linalg.norm(np.cross(B-A,C-A))
print("Cross Product", area1+area2)
