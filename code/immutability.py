# something cannot be changed
my_str = 'testing'
print(my_str.capitalize())
print(id(my_str))

print(id('testing'))

other_str = 'testing'

print(id(other_str) == id(my_str))