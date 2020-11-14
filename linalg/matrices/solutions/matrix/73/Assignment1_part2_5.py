#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
A = np.array([[1,4], [2,5], [3,6]])

b = np.array([[-7,2], [-8,4], [-9,6]])

A_Trans=A.transpose()

A_Trans_A=np.matmul(A_Trans,A)

A_Trans_b=np.matmul(A_Trans,b)

A_Trans_A_inv=np.linalg.inv(A_Trans_A)

x=np.matmul(A_Trans_A_inv,A_Trans_b)

X=x.transpose()


# In[ ]:




