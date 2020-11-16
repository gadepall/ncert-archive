import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability of knowing an answer
p_1= bernoulli_success_prob(0.75)
#Probability of guessing an answer
p_2= 1-p_1
#Probability of getting an answer correct if it is known
p_correct_1= bernoulli_success_prob(1)
#Probability of getting an answer correct if it is guessed
p_correct_2= bernoulli_success_prob(0.25)

#Probability that a correct answer is known
prob= bayes_theorem(p_1,p_2,p_correct_1, p_correct_2)

print(prob)

