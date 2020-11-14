import numpy as np

Q = np.array([[3/np.sqrt(10),-1/np.sqrt(10)],
            [1/np.sqrt(10),3/np.sqrt(10)]])
R = np.array([[np.sqrt(10),np.sqrt(10)],
            [0,np.sqrt(10)]])
res_mat = Q@R

print(res_mat)
