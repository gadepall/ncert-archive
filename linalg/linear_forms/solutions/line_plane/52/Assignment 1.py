import matplotlib.pyplot as plt

x1 = [2,-5/4]
y1 = [-13/7,0]
x2 = [-1,1.5]
y2 = [-2,3]
plt.plot(x1,y1, label= '(4 7)(X) = -5')
plt.plot(x2,y2, label= '(2 -1)(X) = 0')
plt.annotate(" Q (-5/18,-10/18) ", (-5/18,-10/18))
plt.annotate(" P (1,2)", (1,2))
plt.xlabel('x')
plt.ylabel('Y')
plt.title('Intersection of  two lines ')
plt.legend()
plt.grid()
plt.show()
