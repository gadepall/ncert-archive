import numpy

x = [1,2,3]
y = [5,4,3]

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(numpy.arange(0, 50, 0.25))
ax.set_yticks(numpy.arange(0, 50, 0.25))

ax.text(x[0],y[0],"A(1,5)")
ax.text(x[1],y[1],"B(2,4)")
ax.text(x[2],y[2],"C(3,3)")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.scatter(x, y, color = "green")
plt.plot(x,y)
plt.grid()

plt.show()
