import numpy as np

a=2
b=1
D1 = np.array([1,0])
M1 = np.array([[a,-b],[b,a]])
M1inv=np.linalg.inv(M1)
A=M1inv@D1
print("Multiplicative inverse of complex number is ")
print(A)

print(A[0]*a-b*A[1])
print(b*A[0]+a*A[1])