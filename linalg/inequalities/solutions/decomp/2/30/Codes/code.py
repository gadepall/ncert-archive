import numpy as np
Q = np.array([[2/np.sqrt(5),-1/(np.sqrt(5))],[1/np.sqrt(5),2/(np.sqrt(5))]])
R = np.array([[np.sqrt(5),14/np.sqrt(5)],[0,3/(np.sqrt(5))]])
A = Q@R 
print(A)