#Code by GVV Sharma
#November 12, 2019
#Revised Dec 9, 2019
#released under GNU GPL
#Area of a triangle using Hero's formula
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if


#Triangle sides
a = 6
b = 5
c = 4


#Hero's formula
s = (a+b+c)/2
print("Semi-perimieter is",s,"Sides are",a,b,c)
area = np.sqrt(s*(s-a)*(s-b)*(s-c))
print("Hero's formula", area)

