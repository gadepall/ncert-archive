import numpy as np

def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
