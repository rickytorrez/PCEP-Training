print(1 < 2)
print(2 > 1)
print(2 < 1)

print(1 <= 1)

# conversion from floats
print(2.0 >= 3)
print(2.0 >= 2)

# the lower it is alphabetically, the lower it is numerically
print('a' > 'b')
print('b' > 'a')
print('bb' >= 'ba')
print('a' <= 'c')
print(ord('a')) #97

print(1 == 1)
print(1.0 == 1)
print(2 == 1.0)

# not equal
print(1 != 1) #false

# identity operator - has to be the exact same object, same space taken in memory
print(1 is 1) #true

print(1.0 is 1) #false, two distinct objects, diff spots in computer

# id('a') == id('a')
print('a' is not 'a') #false

# check out the id of objects
print(id('a'))

print([] is [])