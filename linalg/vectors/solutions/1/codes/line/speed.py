import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np
import math
from coeffs import *
len=100
# Boy
fig, ax = plt.subplots() 
face=np.array([0,4])
r=0.5
theta = np.linspace(0,2*np.pi,len)
face_circ = np.zeros((2,len))
face_circ[0,:] = r*np.cos(theta)
face_circ[1,:] = r*np.sin(theta)
face_circ = (face_circ.T + face).T
plt.plot(face_circ[0,:],face_circ[1,:],label='boy')
body_base=np.array([0,0])
body_face=np.array([0,3.5])
x_body= line_gen(body_base,body_face)
plt.plot(x_body[0,:],x_body[1,:],label='')
limbs_face=np.array([0,3.5])
limbs_base=np.array([-0.5,2])
limbs1_base=np.array([0.5,2])
x_limbs1= line_gen(limbs_face,limbs1_base)
x_limbs= line_gen(limbs_face,limbs_base)
plt.plot(x_limbs1[0,:],x_limbs1[1,:],label='')
plt.plot(x_limbs[0,:],x_limbs[1,:],label='')

n1 = np.array([1,0]) 
n2 = np.array([0.365,-1]) 
c =  np.array([20,-4]) 
n3 = np.array([0,1])
c3=np.array([4,-4])

#Intercepts
A1,B1 =  line_icepts(n1,c[0])
A2,B2 =  line_icepts(n2,c[1])
A3=np.array([0,4])
B3=np.array([5,4])

#Matrix Ranks
N=np.vstack((n1,n2))
M =np.vstack((N.T, c)).T
#M =np.vstack((n1,n2, c))
rank_N = np.linalg.matrix_rank(N)
rank_M = np.linalg.matrix_rank(M)
m,n = np.shape(N)
##Generating all lines
k1 = 0
k2 = 3
D1=np.linalg.inv(N)@c
print("sol.",D1)
x_A1D1 = line_gen(A1,D1)
x_A2D1 = line_gen(A2,D1)
x_A3B3= line_gen(A3,B3)
#Plotting all lines
plt.plot(x_A1D1[0,:],x_A1D1[1,:],linestyle='dashed',label='Rain initially')
plt.plot(x_A2D1[0,:],x_A2D1[1,:],linestyle='dashed',label='Rain with wind')
plt.plot(x_A3B3[0,:],x_A3B3[1,:],linestyle='dashed',label='')

def get_angle_plot(line1, line2, offset = 5, color = "red", origin = [0,4], len_x_axis = 1, len_y_axis = 1):
    slope1=-(line1[0]/line1[1])
    angle1 = abs(math.degrees(math.atan(slope1)))
    slope2 = -(line2[0]/line2[1])
    angle2 = abs(math.degrees(math.atan(slope2)))
    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)

    angle = theta2 - theta1

    if color is None:
        color = line1.get_color() # Uses the color of line 1 if color parameter is not passed.
    return mpatch.Arc(origin, len_x_axis*offset, len_y_axis*offset, 0, theta1, theta2, color=color, label = str(angle)+u"\u00b0")
angle_plot = get_angle_plot(n2, n3, color="red")

# def get_angle_text(angle_plot):
#     angle = angle_plot.get_label()[:-1] # Excluding the degree symbol
#     angle = "%0.2f"%float(angle)+u"\u00b0" # Display angle upto 2 decimal places

#     # Get the vertices of the angle arc
#     vertices = angle_plot.get_verts()

#     # Get the midpoint of the arc extremes
#     x_width = (vertices[0][0] + vertices[-1][0]) / 2.0
#     y_width = (vertices[0][5] + vertices[-1][6]) / 2.0

#     #print x_width, y_width

#     separation_radius = max(x_width/2.0, y_width/2.0)

#     return [ x_width + separation_radius, y_width + separation_radius, angle]

# angle_text = get_angle_text(angle_plot) 
ax.add_patch(angle_plot) # To display the angle arc
# ax.text(*angle_text)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()