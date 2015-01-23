# 1. Write a script that repeatedly asks the user to input an integer, displaying a message
# to 'try again' by catching the ValueError that is raised if the user did not enter an
# integer; once the user enters an integer, the program should display the number back
# to the user and end without crashing

while(True):
    user_input = raw_input("Enter an integer: ")
    try:
        user_int = int(user_input)
        print 'You entered the integer: {}'.format(user_int)
        break
    except ValueError:
        print 'try again'
        continue
