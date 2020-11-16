import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability of choosing hostelier
p_h= bernoulli_success_prob(0.6)
#Probability of choosing day scholar
p_d= 1-p_h
#Probability of choosing an A grade hostelier
p_A_h= bernoulli_success_prob(0.3)
#Probability of choosing an A grade day scholar
p_A_d= bernoulli_success_prob(0.2)

#Probability that a chosen student with A grade is a hostelier
prob= bayes_theorem(p_h,p_d,p_A_h, p_A_d)

print(prob)

