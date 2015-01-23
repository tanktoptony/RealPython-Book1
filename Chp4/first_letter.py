# Write a script named first_letter.py that first prompts the user for input by using the string:
# Tell me your password:
# The script should then determine the first letter of the user's input, convert that letter to
# upper-case, and display it back. As an example, if the user input was 'no' then the program
# should respond like this: The first letter you entered was: N

user_input = raw_input("Tell me your password: ")
first_letter = user_input[0].upper()
print "The first letter you entered was: %s" % first_letter