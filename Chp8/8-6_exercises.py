# 1. Write a script that uses the randint() function to simulate the toss of a die, returning
# a random number between 1 and 6.
# 2. Write a script that simulates 10,000 throws of dice and displays the average number
# resulting from these tosses.

from __future__ import division
from random import randint
#1
print randint(1,6)

#2
average = 0
for i in range(0,10000):
     average = average + randint(1, 6)

print 'The average of 10,000 throws is {}'.format(average/10000)