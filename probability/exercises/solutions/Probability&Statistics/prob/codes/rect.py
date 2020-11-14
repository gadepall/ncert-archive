
from itertools import product
import matplotlib.pyplot as plt
import math 
import numpy as np

def preprocess(p, x, y, n): 
    for i in range(n): 
        p[i] = x[i] * x[i] + y[i] * y[i]
    p.sort() 
def query(p, n, rad): 
  
    start = 0
    end = n - 1
    while ((end - start) > 1): 
        mid = (start + end) // 2
        tp = math.sqrt(p[mid]) 
  
        if (tp > (rad * 1.0)): 
            end = mid - 1
        else: 
            start = mid 
  
    tp1 = math.sqrt(p[start]) 
    tp2 = math.sqrt(p[end]) 
  
    if (tp1 > (rad * 1.0)): 
        return 0
    elif (tp2 <= (rad * 1.0)): 
        return end + 1
    else: 
        return start + 1
  
if __name__ == "__main__": 
    sample=1000
    x = np.random.uniform(low=-1.5, high=1.5, size=sample)
    y = np.random.uniform(low=-1.0, high=1.0, size=sample)
    circle = plt.Circle((0, 0), 0.5, color='red',fill=False)
    n = len(x) 
    p = [0] * n 
    preprocess(p, x, y, n) 
    event_size=query(p, n, 0.5)
    prob=event_size/sample
    print(prob)
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    plt.scatter(x,y,0.5)
    plt.show()




