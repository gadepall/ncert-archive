# If the two planes are of the form n^T x = c_1 & n^T x = c_2, then the distance between them is given by : abs{c_1-c_2}/norm{vec{n}

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_planes(a1,b1,c1,d1,a2,b2,c2,d2):
    x = np.linspace(-1,1,20)
    y = np.linspace(-1,1,20)

    X,Y = np.meshgrid(x,y)
    Z1 = (d1 - a1*X - b1*Y) / c1
    Z2 = (d2 - a2*X - b2*Y) / c2

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    surf1 = ax.plot_surface(X, Y, Z1)
    surf2 = ax.plot_surface(X, Y, Z2)

    plt.title('Assignment-1 : Parallel Planes')
    plt.show()

def find_distance_bw_planes(a1,b1,c1,d1,a2,b2,c2,d2):
    #To check if planes are parallel
    if (a1/a2 == b1/b2 == c1/c2):
        n1 = np.array([a1,b1,c1,d1])
        n2 = np.array([a2,b2,c2,d2])
        n1 = n1*(a2/a1) 
        distance = abs(n1[3] - n2[3])/np.linalg.norm(n1[:3])
    else:
        print("The given planes are not parallel")
        return -1
    return distance

plot_planes(2,3,4,-4,4,6,8,-12)    
print("The distance between the given parallel planes is : ", find_distance_bw_planes(2,3,4,-4,4,6,8,-12))
