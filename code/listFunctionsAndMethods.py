my_list = [1,2,3]

my_list.append(4) # adds to the end

print(my_list)

my_list.insert(0, 'a') # takes two args, the position and item we want to insert

print(my_list)

print(my_list.index(2)) # looks for the index of an item

print(5 in my_list)

print(2 not in my_list)

other_list = [1,3,4,8,2]

print(other_list)

print(sorted(other_list)) # returns a new list by sorting items in collection

# print(reversed(other_list)) # returns a reversed item

print(list(reversed(other_list)))

print(list(reversed(sorted(other_list)))) # list with only a single type of items
