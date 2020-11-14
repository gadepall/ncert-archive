import matplotlib.pyplot as plt
import numpy as np

# create 1000 eqally spaced points between -10 and 10
x = np.linspace(-2, 2, 100)

# calculate the y value for each element of the x vector
 
y = x**2 + np.sqrt(5)
a = 1
b = 0
c = np.sqrt(5)

d1 = -b + np.sqrt(b**2-4*a*c)
d2 = -b - np.sqrt(b**2-4*a*c)
d1 = d1/(2*a)
d2 = d2/(2*a)

print("The solutions of the equations are",d1,"and",d2)
#x = 0.666,-0.5


fig, ax = plt.subplots()
ax.plot(x, y)
plt.grid()

plt.plot(d2,0, 'o')
plt.text(d2,0.5, 'D')
plt.plot(d1, 0, 'o')
plt.text(d1,0.5, 'E')


#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
#plt.legend(loc='best')

#if using termux
plt.savefig('./figs/conics/q20c.pdf')
plt.savefig('./figs/conics/q20c.eps')
#subprocess.run(shlex.split("termux-open ./line/figs/line_ineq.pdf"))
#else
plt.show()

