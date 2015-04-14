# This script should use a while loop to iterate through the dictionary and 
# grab
# a random state and capital, assigning each to a variable. The user is then
# asked what the capital of the randomly picked state is. The loop continues
# forever, asking the user what the capital is, unless the user either answers
# correctly or types 'exit'.  If the user answers correctly, 'Correct' is
# displayed. However, if the user exits without guessing
# correctly, the answer is displayed along with "Goodbye."

from capitals import capitals_dict
import random


def capital_test(state, capital):
  
  while True:
    answer = input('What is the capital of {}? '.format(state))
    if answer.lower() == 'exit':
      print('The answer was {}, Goodbye!'.format(capital))
      break
    elif answer.lower() == capital.lower():
      print('Correct!')
      break
    

if __name__=='__main__':

  state = random.choice(list(capitals_dict.keys()))
  capital = capitals_dict[state]

  capital_test(state, capital)
  
