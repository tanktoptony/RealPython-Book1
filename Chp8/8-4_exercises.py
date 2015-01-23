# 1. Use a break statement to write a script that prompts the users for input repeatedly,
# only ending when the user types 'q' or 'Q' to quit the program; a common way of
# creating an infinite loop is to write while True:.
# 2. Combine a for loop over a range() of numbers with the continue keyword to print
# every number from 1 through 50 except for multiples of 3; you will need to use the %
# operator.


#1
while(True):
    user_input = raw_input('Enter something ("q" or "Q" to exit): ')
    if user_input == 'q' or user_input == 'Q':
        break


#2
for i in range(1,51):
    if i % 3 == 0:
        continue
    else: 
        print i