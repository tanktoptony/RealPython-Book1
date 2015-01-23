# 1. Create a 'float' object (a decimal number) named weight that holds the value 0.2, and
# create a string object named animal that holds the value 'newt', then use these objects
# to print the following line without using the format() string method: 0.2 kg is the
# weight of the newt.
# 2. Display the same line using format() and empty {} place-holders
# 3. Display the same line using {} place-holders that use the index numbers of the inputs
# provided to the format() method
# 4. Display the same line by creating new string and float objects inside of the format()
# method

#1
weight = 0.2
animal = 'newt'

print str(weight) + ' kg is the weight of the ' + animal + '.'

#2
print '{} kg is the weight of the {}.'.format(weight, animal)

#3
print '{1} kg is the weight of the {0}.'.format(animal, weight)

#4
print '{} kg is the weight of the {}.'.format(0.2, 'newt')