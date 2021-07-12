import numpy as np
import matplotlib.pyplot as plt

#Defining f(x)
def f(x,a,b,d):
	return a*(x**2)+b*x+d
a = 1
b = -2
d = 4

#For maxima using gradient ascent
cur_x = 3
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 2*a*x + b           

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

#For minima 
x1=-3
x2 =4
x3=1
mn=min(f(x1,a,b,d),f(x2,a,b,d),f(x3,a,b,d))

print("Maximum value of f(x) is ",f(cur_x,a,b,d), "at","x =",cur_x)
print("Minimum value of f(x) is ",mn, "at","x =",-np.roots([a,b,-mn])[1])

#Plotting f(x)
x=np.linspace(-6,8,40)
y=x**2-2*x+4
plt.plot(x,y,label='$(x-1)^2+3$')

#Labelling points
plt.plot(cur_x,f(cur_x,a,b,d),'o')
plt.text(cur_x*(1+0.1), f(cur_x,a,b,d)*(1+0.02),'P(-3,19)')
plt.plot(-3,19,'o')
plt.text(-2.5,18,'P(-3,19)')
plt.plot(1,3,'o')
plt.text(1.8,2,'Q(1,3)')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.show()
