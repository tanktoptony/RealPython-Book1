# 1. Create a tuple named cardinal_nums that holds the strings "first",
#'second' and "third" in order

# 2. Display the string at position 2 in cardinal_nums by using an index number

# 3. Copy the tuple values into three new strings named pos1, pos2 and pos3 in
# a single line of code by using tuple unpacking, then print those string value

#1
cardinal_nums = 'first', 'second', 'third'

#2
print cardinal_nums[1]

#3
pos1, pos2, pos3 = cardinal_nums

print("{}, {}, {}".format(pos1, pos2, pos3))