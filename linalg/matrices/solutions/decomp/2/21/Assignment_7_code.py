import numpy as np
A=np.array([[1.,4.],[3.,-5.]])
print("Given matrix A : \n",A)

Q,R=np.linalg.qr(A)

print("\nOrthogonal Matrix Q :\n",Q)

print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R : \n",R)

print("\nA=QR=\n",Q@R)
