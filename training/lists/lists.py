# allows us to batch up a collection of items
my_list = [1,2,3,4,5]
print(my_list)

other_list = ['a',1,1.0, False]
print(other_list)

print(my_list[0]) #1
print(other_list[2]) #1.0

# slicing a list -> gets a list back
print(my_list[0:2]) # [1,2]
print(my_list[1:0]) # [2,3,4,5]

# lists are mutable -> we can modify them
my_list[0] = 'a'
print(my_list)

print(my_list + [8,9,10]) # appends to the end

my_list[1:3] = ['b', 'c']
print(my_list)

my_list = ['a','b','c','d',5,6,7]
my_list[4:] = []
print(my_list)

# removing items form a list with the del statement
del my_list[0] # deletes first index
print(my_list)