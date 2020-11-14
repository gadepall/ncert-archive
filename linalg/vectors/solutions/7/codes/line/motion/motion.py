import numpy as np
import matplotlib.pyplot as plt

V = np.array([[50.91,50.91],[0,51],[0,-51],[50.91,-0.09]])
origin = [0], [0] # origin point
plt.quiver(*origin, V[0][0],V[0][1] , color='r', scale=220,label="$v_w$")
plt.quiver(*origin, V[1][0],V[1][1] , color='b', scale=220,label="$v_b$")
plt.quiver(*origin, V[2][0],V[2][1] , color='g', scale=220,label="$-v_b$")
plt.quiver(*origin, V[3][0],V[3][1] , color='y', scale=220,label="$v_{wb}$")
#plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g','y'], scale=220,label=['velocity'])
plt.legend(loc='upper left')

plt.grid()
plt.show()
