#Code by GVV Sharma
#Dec 9, 2019
#released under GNU GPL
#Circumradius of a triangle
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
area = np.sqrt(s*(s-a)*(s-b)*(s-c))
R = a*b*c/(4*area)
print(R)
