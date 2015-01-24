# Write a script coin_toss.py that uses coin toss simulations to determine the answer to this
# slightly more complex probability puzzle:
# I keep flipping a fair coin until I've seen it land on both heads and tails at least once each - in
# other words, after I flip the coin the first time, I continue to flip it until I get a different result.
# On average, how many times will I have to flip the coin total? Again, the actual probability
# could be worked out, but the point here is to simulate the event using randint(). To get
# the expected average number of tosses, you should set a variable trials = 10000 and a
# variable flips = 0, then add 1 to your flips variable every time a coin toss is made. Then
# you can print flips / trials at the end of the code to see what the average number of
# flips was.

from __future__ import division
from random import randint

trials = 10000
flips = 0 

for i in range(0, trials):
    first_flip = randint(0,1)
    flips += 1 
    while(True):
        if randint(0,1) == first_flip:
            flips += 1 
        else:
            flips += 1 
            break

print 'The average number of flip is {}'.format(flips/trials)