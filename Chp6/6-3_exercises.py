# 1. Write a for loop that prints out the integers 2 through 10, each on a new line, by using
# the range() function
# 2. Use a while loop that prints out the integers 2 through 10 (Hint: you'll need to create
# a new integer first; there's no good reason to use a while loop instead of a for loop in
# this case, but it's good practice)
# 3. Write a function doubles() that takes one number as its input and doubles that number
# three times using a loop, displaying each result on a separate line; test your function
# by calling doubles(2) to display 4, 8, and 16


#1
for num in range(2, 11):
    print num

print ''

#2
counter = 2
while (counter < 11):
    print counter
    counter = counter + 1

print ''

#3
def doubles(num):
    for i in range(3):
        num = num * 2
        print num

doubles(2)