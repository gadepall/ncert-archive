import numpy as np
import matplotlib.pyplot as plt

# Plotting the Lines
x_cor1 = [5, -3]
y_cor1 = [6, -2]
plt.plot(x_cor1, y_cor1, 'r', label='Line')

#  plotting parabola
y = np.linspace(-5, 5, 5000)
x = (y ** 2) / 4
plt.plot(x, y, label='Parabola')

#  plotting point of contact
plt.annotate('P(1,2)',  # this is the text
                 ([1, 2]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(-7, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
plt.scatter(1, 2,color='black')

plt.axis('equal')
plt.legend(loc='best')
plt.grid()
plt.show()
