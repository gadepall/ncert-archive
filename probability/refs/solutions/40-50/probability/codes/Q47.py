import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability of picking red ball
p_1= bernoulli_success_prob(0.5)
#Probability of picking black ball
p_2= 1-p_1
#Probability of getting red ball if first ball is red
p_red_1= bernoulli_success_prob(7/12)
#Probability of getting red ball if first ball is black
p_red_2= bernoulli_success_prob(5/12)

#Probability that a red ball is picked
prob= total_prob(p_1,p_2,p_red_1, p_red_2)

print(prob)

