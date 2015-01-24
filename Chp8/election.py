# Write a script election.py that will simulate an election between two candidates, A and B. One
# of the candidates wins the overall election by a majority based on the outcomes of three regional
# elections. (In other words, a candidate wins the overall election by winning at least
# # two regional elections.) Candidate A has the following odds:
# 87% chance of winning region 1
# 65% chance of winning region 2
# 17% chance of winning region 3
# Import and use the random() function from the random module to simulate events based on
# probabilities; this function doesn't take any arguments (meaning you don't pass it any input
# variables) and returns a random value somewhere between 0 and 1.
# Simulate 10,000 such elections, then (based on the average results) display the probability
# that Candidate A will win and the probability that Candidate B will win.

from __future__ import division
from random import random

total_wins_A = 0
total_wins_B = 0

trials = 10000

for i in range(0, trials):
    A_wins = 0
    B_wins = 0

    #region 1
    if random() < .87:
        A_wins += 1
    else:
        B_wins += 1 

    #region 2
    if random() < .65:
        A_wins += 1 
    else: 
        B_wins += 1 

    #region 3
    if random() < .17:
        A_wins += 1 
    else:
        B_wins += 1

    if A_wins > B_wins:
        total_wins_A += 1 
    else:
        total_wins_B += 1

print 'Probability A will win: {}'.format(total_wins_A/trials)
print 'Probability B will win: {}'.format(total_wins_B/trials)