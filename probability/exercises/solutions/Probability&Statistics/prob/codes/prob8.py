import xlwt
from xlwt import Workbook
import xlrd

import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
from fractions import Fraction
from collections import Counter
import itertools as it
sample =0
n1=0
n2=0
n3=0
wb=Workbook()
my_sheet =wb.add_sheet('Sheet 1')

loc=("./tables/prob8_prob.xlsx")
wb1=xlrd.open_workbook(loc)
sheet=wb1.sheet_by_index(0)

for i in range(0,sheet.nrows):
    for j in range(0,sheet.ncols):
            if sheet.cell_value(i,j)=='':
                my_sheet.write(i,j,sheet.cell_value(i,0)+sheet.cell_value(0,j))
            else:
                my_sheet.write(i,j,sheet.cell_value(i,j))   
wb.save("./tables/prob8_probout.xlsx")                   
loc2=("./tables/prob8_probout.xlsx")
wb2=xlrd.open_workbook(loc2)
sheet1=wb2.sheet_by_index(0)
for t in range(1,sheet1.nrows):
    for k in range(1,sheet1.ncols):
        if sheet1.cell_value(t,k)%2==0:
            n1=n1+1
        if sheet1.cell_value(t,k)==6:
            n2=n2+1
        if sheet1.cell_value(t,k)>=6:
            n3=n3+1
        sample=sample+1
prob1=n1/sample
prob2=n2/sample
prob3=n3/sample
print(prob1," ", prob2, " ", prob3)

