#EE5609:Matrix Theory
#Assignment 1 
#Lines and Planes(Prob.39)
#Verification code-Python Plot
#Code by Sneha Konduru
#Roll no: ee19acmtech11009

#Libraries
import matplotlib.pyplot as plt
import numpy as np


#y= slope*x + intercept 
slope1, intercept1 = (-9/7), (43/7) #  (line1 9x+7y=43)						
slope2, intercept2 = (7/9), (-19/9) #  (line2 7x-9y=19)

#Plot line1 and line2
x  = np.linspace(-10,10,500)

plt.plot(x,x*slope1+intercept1, label='(9 7)x=43')
plt.plot(x,x*slope2+intercept2, label='(7 -9)x=19')

#Limit x and y axes
plt.xlim(-2,8)
plt.ylim(-2,6)

#Verify the points on line1 9x+7y=43
point1 = [22/9,3]
point2 = [4,1]
plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'r*', label='points on (9 7)x=43')
plt.annotate("(22/9,3)", point1)
plt.annotate("(4,1)", point2)

plt.title('Plotting Perpendicular Lines', fontsize=8)
plt.legend()

#plt.savefig("Assignment1.png", bbox_inches='tight')
plt.grid()
plt.show()
