import numpy as np

def dist(A,B):
    return np.sqrt((A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1]))

def tri_hero(a,b,c):
  s = (a+b+c)/2
  area = np.sqrt(s*(s-a)*(s-b)*(s-c))
  return area
  
  
def lieonline(A,O,D):
    return ((D[0]-A[0])*(O[1]-A[1]) == (D[1]-A[1])*(O[0]-A[0]))
      
def dotprod(A,B,C,O):
	V1 = np.array([B[1]-A[1],-B[0]+A[0]])
	V1D = np.array([O[0]-A[0],O[1]-A[1]])
	V2 = np.array([C[1]-B[1],-C[0]+B[0]])
	V2D = np.array([O[0]-B[0],O[1]-B[1]])
	V3 = np.array([A[1]-C[1],-A[0]+C[0]])
	V3D = np.array([O[0]-C[0],O[1]-C[1]])
     	return (np.dot(V1,V1D)>=0 and np.dot(V2,V2D)>=0 and np.dot(V3,V3D)>=0)
 
def lieinterior(A,B,C,O):
	Q = B-A
	W = O-A
	E = C- B
	R = O -B 
	T = A - C
	Y = O- C
	print(np.cross(Q,W))
	print(np.cross(E,R))
	print(np.cross(T,Y))
	
	return (np.cross(Q,W)>=0 and np.cross(E,R)>=0 and np.cross(T,Y)>=0)
  
def interior(A,B,C,O):
    c = (dist(A,B))
    a = (dist(C,B))
    b = (dist(C,A))
    x = (dist(A,O))
    y = (dist(O,B))
    z = (dist(C,O))

    print("Area of ABC",tri_hero(a,b,c))
    print("Area of 3 smaller triangles=",tri_hero(x,y,c) + tri_hero(z,b,x)+ tri_hero(a,z,y) )
    return (np.ceil(tri_hero(a,b,c))==np.ceil((tri_hero(x,y,c) + tri_hero(z,b,x)+ tri_hero(a,z,y))))

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def tri_vert(a,b,c):
  p = (a**2 + c**2-b**2 )/(2*a)
  q = np.sqrt(c**2-p**2)
#Triangle vertices
  A = np.array([p,q]) 
  B = np.array([0,0]) 
  C = np.array([a,0]) 
  return  A,B,C


def line_dir_pt(m,A, dim):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P

#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 
