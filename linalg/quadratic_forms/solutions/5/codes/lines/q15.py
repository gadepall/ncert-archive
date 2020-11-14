import numpy as np
import matplotlib.pyplot as plt
X=[]
Y=[]
l=11
r=40
for i in range(l,r):
    if(i%2==1 and 2*i+2<40):
        X.append(i)
        Y.append(i+2)
print("The following pair of integers satisfy the condition")
for j in range(len(X)):
    plt.text(X[j],Y[j], ((X[j],Y[j])), color='red')
    print(X[j],",",Y[j])

plt.scatter(X,Y)
plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.axis('equal')

plt.savefig('./figs/q15.pdf')
plt.savefig('./figs/q15.eps')

plt.show()
