# 1. Write a script that prompts the user to enter a word using the raw_input() function,
# stores that input in a string object, and then displays whether the length of that string
# is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a
# set of if, elif and else statements.

#1

user_input = raw_input("Enter a word: ")

if len(user_input) < 5:
    print 'less that 5 characters'
elif len(user_input) > 5:
    print 'greater that 5 characters'
else:
    print 'equal to 5 characters'