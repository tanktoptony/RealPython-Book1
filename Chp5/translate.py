# Write a script translate.py that asks the user for some input with the following prompt:
# Enter some text:
# You should then use the replace() method to convert the text entered by the user into
# 'leetspeak' by making the following changes to lower-case letters:
# The letter: a becomes: 4
# The letter: b becomes: 8
# The letter: e becomes: 3
# The letter: l becomes: 1
# The letter: o becomes: 0
# The letter: s becomes: 5

user_input = raw_input("Enter some text: ")

user_input = user_input.replace('a', '4')
user_input = user_input.replace('b', '8')
user_input = user_input.replace('e', '3')
user_input = user_input.replace('l', '1')
user_input = user_input.replace('o', '0')
user_input = user_input.replace('s', '5')

print user_input