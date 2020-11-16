import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability of choosing bag1
p_bag1= bernoulli_success_prob(0.5)
#Probability of choosing bag2
p_bag2= bernoulli_success_prob(0.5)
#Probability of drawing red ball from bag1
p_red_bag1= bernoulli_success_prob(0.5)
#Probability of drawing red ball from bag2
p_red_bag2= bernoulli_success_prob(0.25)

#Probability that a red ball is drawn from bag1
prob= bayes_theorem(p_bag1,p_bag2,p_red_bag1, p_red_bag2)

print(prob)


