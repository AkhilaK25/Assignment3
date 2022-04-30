import numpy as np
from numpy import random as RN 
#Theoritical probabilities
marbles = 9
white = 2
blue = 3
red = 4
PrW = white/marbles
PrB = blue/marbles
PrR = red/marbles
print("Theoritical probabilities:",PrW,PrB,PrR)

#Experimental probabilities
#Sample size
N = 9

#Generating Events
x = RN.randint(0, high = 3, size=N)

pr_0 = np.count_nonzero(x==0)
pr_1 = np.count_nonzero(x==1)
pr_2 = N - pr_0 - pr_1

print("Random Probabilities:", pr_0/N, pr_1/N, pr_2/N)

