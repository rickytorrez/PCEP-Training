# lists are mutable

my_list = [1, 2, 3, 4, 5]
print(my_list)

other_list = ['a', 1, 2.0, False]
print(other_list)

print(my_list[0])
print(my_list[2])

print(my_list[0:2])
print(my_list[1:])
print(my_list[:3])
print(my_list[0::1])

my_list[0] = 'a' # mutable
print(my_list)

my_list += [8,9,10]

print(my_list)

my_list[1:3] = ['b', 'c']
print(my_list)

del my_list[0]
print(my_list)

