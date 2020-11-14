import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import math

P = [2.25, 3.3072]
Q = [0,0]
R = [6,0]
S = [8/3,0] #found using triangle angle bisector theorem

mag_SP = np.sqrt((S[0]-P[0])**2+(S[1]-P[1])**2)
mag_SQ = np.sqrt((S[0]-Q[0])**2+(S[1]-Q[1])**2)
mag_SR = np.sqrt((S[0]-R[0])**2+(S[1]-R[1])**2)

l_SP = [P[0]-S[0],P[1]-S[1]] 
l_SQ = [Q[0]-S[0],Q[1]-S[1]]
l_SR = [R[0]-S[0],R[1]-S[1]]

dot_PSR = (l_SP[0]*l_SR[0])+(l_SP[1]*l_SR[1])
dot_PSQ = (l_SP[0]*l_SQ[0])+(l_SP[1]*l_SQ[1])

cang_PSR = (dot_PSR)/(mag_SP*mag_SR)
cang_PSQ = (dot_PSQ)/(mag_SP*mag_SQ)


ang_PSR = math.acos(cang_PSR)*(180/3.14)
ang_PSQ = math.acos(cang_PSQ)*(180/3.14)
#(180/3.14) is to convert radians into degrees

print("angle PSQ",ang_PSQ)
print("angle PSR",ang_PSR)
