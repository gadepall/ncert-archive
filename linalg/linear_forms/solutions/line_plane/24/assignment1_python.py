import numpy as np
import matplotlib.pyplot as plt


def show(titles): 
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.title(titles)
    plt.show()

def midpoint(BP):
    
    arr = []
    sum1 =0
    sum2 =0
    for j in range(len(BP)):
        sum1 += BP[j][0]
        sum2 += BP[j][1]
    sum1 = 1/2 *sum1
    sum2 = 1/2 *sum2
    arr.append(sum1)
    arr.append(sum2)

    return arr

origin = [0,0]
print("Given are the points : [8,0] and [0,-4]")
B_P = [[8,0],[0,-4]]
x1 = [B_P[0][0],B_P[1][0]]
y1 = [B_P[0][1],B_P[1][1]]


for i in range(len(B_P)): 
    plt.scatter(B_P[i][0],B_P[i][1],color='blue')
show("Point P[0,-4] and B[8,0]")

print(" The line joining the two points is given in the visualization ")
for i in range(len(B_P)): 
    plt.scatter(B_P[i][0],B_P[i][1],color='blue')

plt.plot(x1,y1,color='blue')
show("Line joining the points P and B")

print(" The midpoint of the line segment is 1/2*(P+B) which is shown in the visualization")
midpoint1 = midpoint(B_P)
print(" The midpoint of the line segment is :",midpoint1)

for i in range(len(B_P)): 
    plt.scatter(B_P[i][0],B_P[i][1],color='blue')
plt.plot(x1,y1,color='blue')
plt.scatter(midpoint1[0],midpoint1[1],color='red')
show(" The midpoint of the line marked in red")

print(" The line joining the origin and the midpoint is show in the visualization")

print(" the slope is calculated by m = (y2-y1)/(x2-x1) ")

slope = (midpoint1[1]-origin[1]) / (midpoint1[0]-origin[0]) 
print(" Hence the slope is : m = ",slope)

for i in range(len(B_P)): 
    plt.scatter(B_P[i][0],B_P[i][1],color='blue')
plt.plot(x1,y1,color='blue')
plt.scatter(midpoint1[0],midpoint1[1],color='red')
plt.scatter(origin[0],origin[1],color='red')
plt.plot([origin[0],midpoint1[0]],[origin[1],midpoint1[1]],color='red')

show(" The line segment joining the origin and the midpoint ")
