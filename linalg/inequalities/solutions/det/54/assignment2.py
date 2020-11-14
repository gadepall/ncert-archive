#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-30,30,10)
y1 = (5-x)/3
y2 = (8-2*x)/6
plt.plot(x,y1, label = 'x+3y = 5')
plt.plot(x,y2, label = '2x+6y = 8')
plt.axis("equal")

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid() 


# In[ ]:




