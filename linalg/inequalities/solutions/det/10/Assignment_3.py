import numpy as np
a=1;
b=2;
c=3;
A= np.array([[a-b,b-c,c-a],[b-c,c-a,a-b],[c-a,a-b,b-c]])
d = np.linalg.det(A)

print('|A| = ', d)