import numpy as np
import math
import matplotlib.pyplot as plt

t=math.pi/3

A=np.array([[math.cos(t),math.sin(t)],[-math.sin(t),math.cos(t)]])

B=np.array([[math.sin(t),-math.cos(t)],[math.cos(t),math.sin(t)]])

Result=math.cos(t)*A+math.sin(t)*B

print(Result)
