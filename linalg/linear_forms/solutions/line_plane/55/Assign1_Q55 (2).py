import matplotlib.pyplot as plt
a=1;
b=3;
c=7;
x1=3;
y1=8;

import numpy as np

m = np.array([[b], [-a]]);
n = np.array([[a],[b]]);
P = np.array([[x1],[y1]]);

m1 = m.transpose()
n1 = n.transpose()

den = (m1 @ m) + (n1 @ n);
num = ( (m @ m1) - (n @ n1) ) @ P;

n11= pow(a,2)+pow(b,2);

x = (num/den) + (c/n11) * n;
R=2*x;

x = np.linspace(-15,15,500)

e = (c-a*x)/b;
plt.plot(x, e)

f = P[1] + ( (x-P[0]) * ((R[1]-P[1])/(R[0]-P[0])))

plt.annotate("(3,8)", (P[0], P[1]))
plt.annotate("(-1,-4)", (R[0], R[1]))
plt.grid()

plt.plot(x, f)

plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')


plt.xlim(-15,15)
plt.ylim(-15,15)

plt.show()
plt.savefig("image_of_point_in_2D_line.png", bbox_inches='tight')
