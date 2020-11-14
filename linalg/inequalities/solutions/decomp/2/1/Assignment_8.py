import numpy as np
Q=np.array([[0.448,-0.896],[0.896,0.448]])
R=np.array([[2.23,2.23],[0,2.23]])
result=Q@R
print(result)
