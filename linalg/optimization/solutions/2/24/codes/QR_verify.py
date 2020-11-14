import numpy as np
Q=np.array([[0.6,0.8],[-0.8,0.6]])
R=np.array([[5,-2.2],[0,0.4]])
A=Q@R
I=Q.T@Q
print('The given matrix obtained from Q and R:',A)
print('Proving that Q^TQ is :',I)
