#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
V=np.array([[12,3.5],
            [3.5,-10]], dtype=float)

print("Given matrix V is, \n",V)

Q,R=np.linalg.qr(V)

print("Orthogonal Matrix Q :\n",Q)

print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R : \n",R)

print("\nA=QR=\n",Q@R)


# In[ ]:




