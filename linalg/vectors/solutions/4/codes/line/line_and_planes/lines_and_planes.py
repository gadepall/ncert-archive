# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x1 = np.linspace(-5,5,300)
y1 = (9.35 - 2*x1)/3

x2 = np.linspace(-5,5,300)
y2 = 5*x2 - 50

x3 = np.linspace(-5,5,300)
y3 = (6 + 2*x3)/3

x4 = np.linspace(-5,5,300)
y4 = (x4)/3

x5 = np.linspace(-5,5,300)
y5 = (-2*x5)/5

P1= np.array([4.67, 0])
Q1 = np.array([0, 3.116])

P8= np.array([-2.25, 3])
Q8 = np.array([-2.25, 1])

P3= np.array([-3, 0])
Q3 = np.array([0, 2])

P4= np.array([0, 0])
Q4 = np.array([3, 1])

P5= np.array([0, 0])
Q5 = np.array([1, 2])

P6= np.array([-0.66, 0])
Q6 = np.array([-0.66, 3])

P7= np.array([3, 2])
Q7 = np.array([-3, 2])


# Create the plot
plt.plot(x1,y1,label='3y+2x=9.35')
#plt.plot(x2,y2,label='5x-y=50')
plt.plot(x3,y3,label='3y-2x=6')
plt.plot(x4,y4,label='3y=x')
plt.plot(x5,y5,label='5y+2x=0')
plt.axvline(x=-0.66,label='x=-2/3')
plt.axhline(y=2,label='y=2')
plt.axvline(x=-2.5,label='x=-5/2')

plt.plot(P1[0],P1[1],'o')
plt.text(P1[0]*(1+0.1), P1[1]*(1-0.1), 'P1')
plt.plot(Q1[0],Q1[1],'o')
plt.text(Q1[0]*(1-0.2), Q1[1]*(1), 'Q1')

plt.plot(P3[0],P3[1],'o')
plt.text(P3[0]*(1+0.1), P3[1]*(1-0.1), 'P3')
plt.plot(Q3[0],Q3[1],'o')
plt.text(Q3[0]*(1-0.2), Q3[1]*(1), 'Q3')

plt.plot(P4[0],P4[1],'o')
plt.text(P4[0]*(1+0.1), P4[1]*(1-0.1), 'P4')
plt.plot(Q4[0],Q4[1],'o')
plt.text(Q4[0]*(1-0.2), Q4[1]*(1), 'Q4')

plt.plot(P5[0],P5[1],'o')
plt.text(P5[0]*(1+0.1), P5[1]*(1-0.1), 'P5')
plt.plot(Q5[0],Q5[1],'o')
plt.text(Q5[0]*(1-0.2), Q5[1]*(1), 'Q5')

plt.plot(P6[0],P6[1],'o')
plt.text(P6[0]*(1+0.1), P6[1]*(1-0.1), 'P6')
plt.plot(Q6[0],Q6[1],'o')
plt.text(Q6[0]*(1-0.2), Q6[1]*(1), 'Q6')

plt.plot(P7[0],P7[1],'o')
plt.text(P7[0]*(1+0.1), P7[1]*(1-0.1), 'P7')
plt.plot(Q7[0],Q7[1],'o')
plt.text(Q7[0]*(1-0.2), Q7[1]*(1), 'Q7')

plt.plot(P8[0],P8[1],'o')
plt.text(P8[0]*(1+0.1), P8[1]*(1-0.1), 'P8')
plt.plot(Q8[0],Q8[1],'o')
plt.text(Q8[0]*(1-0.2), Q8[1]*(1), 'Q8')

# Add a title
plt.title('lines and planes ')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
plt.savefig('../figures/line/lines_and_planes/lines_and_planes.eps')
# Show the plot
plt.show()
