# 1. In one line, display the result of trying to find() the substring 'a' in the string 'AAA';
# the result should be -1
# 2. Create a string object that contains the value 'version 2.0'; find() the first occurrence
# of the number 2.0 inside of this string by first creating a 'float' object that stores the
# value 2.0 as a floating-point number, then converting that object to a string using the
# str() function
# 3. Write and test a script that accepts user input using raw_input(), then displays the
# result of trying to find() a particular letter in that input


#1
print 'AAA'.find('a')

#2
my_str = 'version 2.0'
my_float = 2.0
print my_str.find(str(my_float))

#3
my_input = raw_input("Enter a string: ")
print my_input.find('b')
