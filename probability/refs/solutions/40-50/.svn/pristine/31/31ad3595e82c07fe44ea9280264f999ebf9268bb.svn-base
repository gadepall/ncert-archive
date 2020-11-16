import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
from functions import *

data_binom = binom.rvs(n=2,p=8/18,size=10000)
#Probability of picking red ball
p_1= bernoulli_success_prob(8/18)

#Probability that both balls are red
print(np.count_nonzero(data_binom==2)/10000)

#Probability that first is black and second is red
print((1-p_1)*p_1)

#Probability that one is black and other is red
print(np.count_nonzero(data_binom==1)/10000)

