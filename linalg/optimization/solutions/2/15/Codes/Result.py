import numpy as np
import math

Q = np.array([[2/math.sqrt(13),3/math.sqrt(13)],
              [3/math.sqrt(13),-2/math.sqrt(13)]])
R = np.array([[math.sqrt(13),-6/math.sqrt(13)],
              [0,17/math.sqrt(13)]])
M = Q@R
print(M)
