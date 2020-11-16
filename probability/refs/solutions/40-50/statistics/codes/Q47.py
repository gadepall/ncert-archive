
import numpy as np
from scipy import stats

data = [41, 39, 48, 52, 46, 62, 54, 40, 96, 52, 98, 40, 42, 52, 60]
data.sort()

mean = np.mean(data)

median = np.median(data)

mode = stats.mode(data)

print('Mean is ', mean)
print('Median is ' , median)
print('Mode is ' , mode)

