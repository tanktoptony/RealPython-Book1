# 1. Write a cube() function that takes a number and multiplies that number by itself twice
# over, returning the new value; test the function by displaying the result of calling your
# cube() function on a few different numbers
# 2. Write a function multiply() that takes two numbers as inputs and multiples them
# together, returning the result; test your function by saving the result of multiply(2,
# 5) in a new integer object and printing that integer's value


#1
def cube(num):
    return num**3

# 2
def multiply(num_1, num_2):
    return num_1 * num_2


if __name__=='__main__':
    #1 test
    print cube(3)
    print cube(2)
    print cube(9)

    print ''
    #2 test
    test_1 = multiply(5, 2)
    test_2 = multiply(8, 6)
    print test_1
    print test_2