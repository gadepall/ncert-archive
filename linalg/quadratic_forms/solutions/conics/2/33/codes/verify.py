import numpy as np
A=np.array([[6.,1.],[-8.,2.]])
print("Given matrix A : \n",A)

Q,R=np.linalg.qr(A)

print("\n Orthogonal Matrix Q :\n",Q)

print("\n Q^TQ :\n",Q.T@Q)

print("\n Upper Triangular Matrix R : \n",R)

print("\n A=QR= \n",Q@R)
