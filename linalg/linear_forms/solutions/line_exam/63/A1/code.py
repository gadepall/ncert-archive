import numpy as np
import matplotlib.pyplot as plt
import math

def norm(x):
    return np.sqrt(np.sum(np.square(x)))


a = np.array((1, 1, -1)).reshape(3,1)
b = np.array((1, -1, 1)).reshape(3,1)

cos_theta = np.matmul(a.T, b)/(norm(a)*norm(b))
print("The value of cos Theta is", cos_theta[0][0])
print("The value of Theta in radians is", math.acos(cos_theta))
print("The value of Theta in degrees is", math.acos(cos_theta)*180/np.pi)

