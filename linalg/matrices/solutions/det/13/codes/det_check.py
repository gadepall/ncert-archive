import numpy as np

a=1
b=2
c=3
p=4
q=5
r=6
x=7
y=8
z=20
m = np.array([[b+c, q+r, y+z], [c+a, r+p, z+x], [a+b,p+q,x+y]])
print(m)

det_m =np.linalg.det(m)
print(det_m)

#m_1[0]=m[0]+m[1]+m[2]
n_1=np.array([m[0]+m[1]+m[2],m[1],m[2]])
print(n_1)

n_2=np.array([n_1[0]/2,m[1]-n_1[0]/2,m[2]-n_1[0]/2])
print(n_2)

n_3=np.array([n_2[0]+n_2[1]+n_2[2],n_2[1],n_2[2]])
print(n_3)

n_4=(-1)**2 * np.array([n_3[0],(-1)*n_3[1],(-1)*n_3[2]])
print(n_4)


d=np.linalg.det(n_4)
print(2*d)

if 2*d == det_m:
   print("matched")
