import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,120,100)
y1 = 60-(x1/2)

x2 = np.linspace(0,120,100)
y2 = 60-x2

x3 = np.linspace(0,120,100)
y3 = (x3/2)

x4=[60,40,60,120]
y4=[30,20,0,0]


plt.scatter(x4,y4,color='b')
plt.annotate("A",(60,30))
plt.annotate("B",(40,20))
plt.annotate("C",(60,0))
plt.annotate("D",(120,0))

plt.fill(x4,y4)





plt.plot(x1, y1, '-b')
plt.plot(x2, y2, '-r')
plt.plot(x3, y3, '-g')

plt.xlabel('x', color='b')
plt.ylabel('y', color='g')


plt.title('All lines')
plt.axhline()
plt.axvline()

plt.grid()
plt.show()