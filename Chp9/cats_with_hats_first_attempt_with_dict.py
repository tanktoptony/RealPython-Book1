# You have 100 cats
# One day you decide to arrange all your cats in a giant circle. Initially, none 
# of your cats have any hats on. You walk around the circle 100 times, always 
# starting at the same spot, with the first cat (cat #1). Every time you stop
# at a cat, you either put a hat on it if it doesn’t have one
# on, or you take its hat off if it has one on.

# The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat (#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats
# (e.g., you only visit the 100th cat).

# Write a program that simply outputs which cats have hats at the end.

cats = {}

for i in range(1, 101):
  cats['cat' + str(i)] = False


def put_on_hats():
  #round 1
  for key in cats:
    cats[key] = True

  
  for round in range(2, 101):
    for cat in range(1, 101):
      if cat % round == 0:
        if cats['cat' + str(cat)] == False:
          cats['cat' + str(cat)] = True
        else:
          cats['cat' + str(cat)] = False


put_on_hats()


for c, hats in cats.items():
  #print(c + ':' + cats[c])
  if cats[c] == True:
    print(c + ' has a hat.')

  




