# Write a script factors.py that includes a function to find all of the integers that divide
# evenly into an integer provided by the user. A sample run of the program should look
# like this (with the user's input highlighted in bold):

def factor(user_number):
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            print '{} is a divisor of {}'.format(i, user_number)

if __name__=='__main__':
    user_input = int(raw_input('Enter a number: '))
    factor(user_input)

