import numpy as np
import matplotlib.pyplot as plt
#Plotting all lines
x = np.linspace(-10, 10, 40)
y= (12-4*x)/3
plt.plot(x,y, label ='4x+3y=12')
plt.xlim(-8,8)
plt.ylim(-12,12)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() 

# y-axis values 
x = [3,0,0]
y = [4,-8,10.67] 
  
# plotting points as a plot 
plt.plot(0,-8, 'ro', label = 'P2(0,a)')
plt.plot(0,4, 'ro', label = 'P1(0,4)')
plt.plot(0,10.67, 'ro', label = 'P3(0,b)')

  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('line plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 





