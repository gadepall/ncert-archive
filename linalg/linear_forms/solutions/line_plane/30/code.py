import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100)
y = -x/7
plt.plot(x, y, '-r', label='y=-x/7 and Y-intercept = 0')
plt.plot(x, y, '-b', label='Direction Vector')
plt.plot(x, y, '-r', label='')
plt.title('Question:30.a : Graph of y=-x/7')
#plt.xlabel('x', color='#555555')
#plt.ylabel('y', color='#555555')
plt.legend(loc='upper left')
plt.grid()
plt.arrow(0, 0, 7, -1, width = 0.03)  
# x axis values 
x = [0, 0] 
# corresponding y axis values 
y = [0, 0] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=5) 
plt.show()


x = np.linspace(-3,3,100)
y = -2*x+5/3
plt.plot(x, y, '-r', label='y=-2x+5/3 and Y-intercept = 5/3')
plt.plot(x, y, '-b', label='Direction Vector')
plt.plot(x, y, '-r', label='')
plt.title('Question:30.b:Graph of y=-2x+5/3')
#plt.xlabel('x', color='#555555')
#plt.ylabel('y', color='#555555')
plt.legend(loc='upper left')
plt.grid()
plt.arrow(0, 0, -5/6, 5/3, width = 0.03) 
# x axis values 
x = [0, 0] 
# corresponding y axis values 
y = [0, 5/3] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=5) 
plt.show()



x = np.linspace(-4,4,300)
y = 0*x
plt.plot(x, y, '-r', label='y=0 and Y-intercept = 0')
plt.plot(x, y, '-b', label='Direction Vector')
plt.plot(x, y, '-r', label='')
plt.title('Question:30. : Graph of y=0')
#plt.xlabel('x', color='#555555')
#plt.ylabel('y', color='#555555')
plt.legend(loc='upper left')
plt.grid()
plt.arrow(0, 0, 3, 0, width = 0.001) 
# x axis values 
x = [0, 0] 
# corresponding y axis values 
y = [0, 0] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=5) 
plt.show()
