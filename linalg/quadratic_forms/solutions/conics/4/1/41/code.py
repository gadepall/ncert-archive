import numpy as np
A=np.array([[12,-5],
            [-5,2]], dtype=float)

print("Given matrix A is, \n",A)

Q,R=np.linalg.qr(A)

print("Orthogonal Matrix Q :\n",Q)

print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R : \n",R)

print("\nA=QR=\n",Q@R)
