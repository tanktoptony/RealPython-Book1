# 1. Create a list named desserts that holds the two string values 'ice cream' and 'cookies'
# 2. Sort desserts in alphabetical order, then display the contents of the list
# 3. Display the index number of 'ice cream' in the desserts list
# 4. Copy the contents of the desserts list into a new list object named food
# 5. Add the strings 'broccoli' and 'turnips' to the food list
# 6. Display the contents of both lists to make sure that 'broccoli' and 'turnips' haven't
# been added to desserts
# 7. Remove 'cookies' from the food list
# 8. Display the first two items in the food list by specifying an index range
# 9. Create a list named breakfast that holds three strings, each with the value of 'cookies',
# by splitting up the string 'cookies, cookies, cookies'
# 10. Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument
# and then outputs only the numbers from the list that fall between 1 and 20
# (inclusive)


#1
desserts = ['ice cream', 'cookies']

#2
desserts.sort()

#3
print desserts.index('ice cream')

#4
food = desserts[:]

#5
food.extend(['broccoli', 'turnips'])

#6
print desserts
print food 

#7
food.remove('cookies')

#8
print food[0:2]

#9
breakfast = 'cookies, cookies, cookies'.split(', ')

#10
def print_range(my_list):
    for i in my_list:
        if i >= 1 and i <= 20:
            print i
                
print_range([2, 4, 8, 16, 32, 64])