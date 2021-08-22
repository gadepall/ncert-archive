import numpy as np
from matplotlib import pyplot as plt

AT = np.array([[3, 4], [-1, 2], [0, 1]])
B = np.array([[-1, 2, 1], [1, 2, 3]])

BT=B.T
A=AT.T

print("(A+B)'=\n",(A+B).T)
print("A'+B'=\n",(AT+BT))

comparison = (AT+BT)==(A+B).T
equal_arrays = comparison.all()


if (equal_arrays):
  print('Hence, verified')
else:
  print('They are not equal')