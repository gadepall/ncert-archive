import xlwt
from xlwt import Workbook
import xlrd

import numpy as np
from scipy.stats import norm
#import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
from fractions import Fraction
from collections import Counter
import itertools as it

class Pmf(Counter):
    """A Counter with probabilities."""
    
    
    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of values from the
        two distributions.

        other: Pmf

        returns: new Pmf
        """
        
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def __hash__(self):
        """Returns an integer hash value."""
        
        return id(self)

    def __eq__(self, other):
        return self is other

    def render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))
        
d6 = Pmf([1,2,3,4,5,6])
d6.normalize()
d6_twice = (d6 + d6)
d6_twice.name = 'two dice'
for die in [d6_twice]:
    xs, ys = die.render()

wb=Workbook()
my_sheet =wb.add_sheet('Sheet 1')
my_sheet.write(0,0,"Event")
my_sheet.write(0,1,"Value")

loc=("./tables/input.xlsx")
wb1=xlrd.open_workbook(loc)
sheet=wb1.sheet_by_index(0)

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)==xs[i-1]:
        my_sheet.write(i,0,xs[i-1])
        if sheet.cell_value(i,1)=='-':
            my_sheet.write(i,1,ys[i-1])
        else:
            my_sheet.write(i,1,sheet.cell_value(i,1) )      

wb.save("./tables/output.xlsx")
