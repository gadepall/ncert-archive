import numpy as np
A=np.array([[2.,-6.],[1.,-2.]])
print("Given matrix A is: \n",A)
Q,R=np.linalg.qr(A)
print("\nOrthogonal Matrix Q is :\n",Q)
#Verification Q^TQ=I
print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R is: \n",R)
print("\nA=QR=\n",Q@R)
