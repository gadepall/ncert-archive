'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


import math

from scipy import stats
X = stats.binom(6, 2/3) # Declare X to be a binomial random variable
print("Probability that in the next 6 trials, there will be atleast 4 successes")
print (X.pmf(4)+X.pmf(5)+X.pmf(6),"\n")          # P(X = 0)
  
