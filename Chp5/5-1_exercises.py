# 1. Create a string object that stores an integer as its value, then convert that string into
# an actual integer object using int(); test that your new object is really a number by
# multiplying it by another number and displaying the result
# 2. Repeat the previous exercise, but use a floating-point number and float()
# 3. Create a string object and an integer object, then display them side-by-side with a single
# print statement by using the str() function


# String holding an in t value
number_string = '3'

# cast into an int multiple by 5. Display the result 
print int(number_string) * 5

# string holding a float value
float_string = '2.03'

# cast to float and multiple by 5. Display result
print float(float_string) * 5

# create string and int object.  cast theint and concatenate with the string object
my_str = 'Hello '
my_int = 4
print my_str + str(my_int)
