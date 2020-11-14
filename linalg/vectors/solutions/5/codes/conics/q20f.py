import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 2.5, 100)
 
y = x**2  -(np.sqrt(2))*x + 0.33
a = 1
b =-np.sqrt(2)
c =0.33

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
plt.savefig('./figs/conics/q20f.pdf')
plt.savefig('./figs/conics/q20f.eps')
#subprocess.run(shlex.split("termux-open ./line/figs/line_ineq.pdf"))
#else
plt.show()

