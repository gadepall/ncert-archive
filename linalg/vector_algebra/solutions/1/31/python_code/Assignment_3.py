import matplotlib.pyplot as plt

x1 = [0,3,0,-3,-3,3]
y1 = [6,0,6,0,0,0]
x2 = [-3,1.5]
x3 = [3,-1.5]
y2 = [0,3]
y3 = [0,3]

plt.rc('xtick', labelsize=10) 
plt.rc('ytick', labelsize=10)
plt.rcParams.update({'font.size': 10})
plt.xlim(-4,4)
plt.ylim(-.2, 8)
plt.plot(x1,y1 )
plt.plot(x2,y2 )
plt.plot(x3,y3 )
plt.annotate(" E ", (1.5,3)) ## for Showing vertex clearly
plt.annotate(" F", (-1.8,3)) ## for Showing vertex clearly
plt.annotate(" A", (0,6)) ## for Showing vertex clearly
plt.annotate(" B ", (-3.3,0)) ## for Showing vertex clearly
plt.annotate(" C ", (3,0))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Isosceles Triangle ')
plt.show()
