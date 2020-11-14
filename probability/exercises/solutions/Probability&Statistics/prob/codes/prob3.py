import numpy as np
from scipy.stats import norm
import seaborn as sns
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
data=random.choice(xs,p=ys,size=(1000))
print(xs[0],ys)
# ax = sns.distplot(data,
# 					bins=int(11),
# 	                 kde=True,
# 	                color='crimson',
#                   hist_kws={"linewidth": 20,'alpha':0.5})
# ax.set(xlabel='Sum_of_two_dice', ylabel='Probability')
# plt.show()
