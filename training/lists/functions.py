# list functions and methods

my_list = [4,3,2,1]

# adds to the end of list
my_list.append(4)

print(my_list)

# insert something in a particular position
# takes two arguments
# position -> index where we want to insert at
# item -> what we want to insert
# doesn't replace but shift
my_list.insert(0, 'a')

print(my_list)

# know what is in the actual position of an index that is on a list
# use index method
print(my_list.index(2))

# in and not in operations (index)
my_list = [1,2,3]
print(4 in my_list) # false
print(4 not in my_list) # true

my_new_list = [1,3,7,2,8]
# sort an unordered list
print(sorted(my_new_list))

# reverse a list
# returns a reversed object initially
print(reversed(my_list)) #<list_reverseiterator object at 0x7f3b6217a210>

# convert it back into a list
# print(list(reversed(my_new_list))) [8,2,7,3,1]

# return a sorted reversed list
print(list(reversed(sorted(my_new_list))))