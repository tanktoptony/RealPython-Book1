import random


def select_words(available_words):
  word_list = []
  while len(word_list) < 3:
    choice = random.choice(available_words)
    if choice in word_list:
      continue
    else:
      word_list.append(choice)
  return word_list


def make_poem():
  
  """ returns a multiline string poem"""

  my_nouns = select_words(nouns)
  my_verbs = select_words(verbs)
  my_adverbs = select_words(adverbs)
  my_prepositions = select_words(prepositions)
  my_adjectives = select_words(adjectives)
  starting_word = "A"
  a_an = 'a'
  if my_adjectives[0] == 'incredulous' or my_adjectives[0] == 'exuberant':
    starting_word = 'An'
  if my_adjectives[2] == 'incredulous' or my_adjectives[2] == 'exuberant':
    a_an = 'an'


  print("""{} {} {} \n\n{} {} {} {} {} the {} {}\n{}, the {} {}\nthe {} {} {} {} {} {}
  """.format(starting_word, my_adjectives[0], my_nouns[0], starting_word, my_adjectives[0], my_nouns[0], my_verbs[0], my_prepositions[0], my_adjectives[1], my_nouns[1], my_adverbs[0], my_nouns[0], my_verbs[1], my_nouns[1], my_verbs[2], my_prepositions[1], a_an,  my_adjectives[2], my_nouns[2]
      ))
  
  
if __name__=='__main__':
  
  nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

  verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

  adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

  prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

  adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

  make_poem()


      
