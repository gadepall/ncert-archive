import numpy as np
import math

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

def angleBisector(A, B, C):
  a = np.linalg.norm(dir_vec(A,B))
  b = np.linalg.norm(dir_vec(A,C))
  temp_ang_bis = dir_vec(A,C)/b + dir_vec(A,B)/a
  return temp_ang_bis

def findingTheThirdCoord(side_length, angA, angB): 
  a = 1 - (np.cos(np.pi/180 * angB))**2 - (np.tan(np.pi / 180 * angA) * np.cos(np.pi / 180 * angB))**2
  b = -(2 * side_length) + (2 * side_length * np.cos(np.pi / 180 * angB)**2)
  c = side_length**2 - (side_length * np.cos(np.pi / 180 * angB))**2
  if angA > 90 or angB > 90:
    A = (-b + math.sqrt(b**2 - 4*a*c))/ (2 * a)
  else:
    A = (-b - math.sqrt(b**2 - 4*a*c))/ (2 * a)
  B = A * np.tan(np.pi / 180 * angA)
  return np.array([A, B])

def findAngle(A, B, C):
  a = np.array(dir_vec(A, C))
  b = np.array(dir_vec(A, B))
  return np.arccos( np.sum(a*b) / (np.linalg.norm(a) * np.linalg.norm(b)) ) * 180 / np.pi

def circumCenter(A, B, C):
  angA = findAngle(A, B, C)
  angB = findAngle(B, A, C)
  angC = findAngle(C, B, A)
  return (A * np.sin(np.pi * angA / 180 * 2) + B * np.sin(np.pi * angB / 180 * 2) + C * np.sin(np.pi * angC / 180 * 2))/(np.sin(np.pi * angA / 180 * 2) + np.sin(np.pi * angB / 180 * 2) + np.sin(np.pi * angC / 180 * 2))

def toFinddim(A):
  print(f'dimensions possible for matrix size of {A}')
  for x in range(1, A+1, 1):
    if A%x == 0:
      print(f'{x} x {int(A/x)}' )

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 
