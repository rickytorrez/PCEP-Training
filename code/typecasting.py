# how we move one object from one type to another
# integer to float

print(1)

print(float(1))

print(int(1.3))

# does not round, it truncates everything that is after the decimal point and
# just get rid of it
print(int(1.6))

print(str(1))

print(str(1.0))

print(str(False))

print(int('1'))

print(float('1'))

print(float('1.2'))

print(bool(1))

print(bool(2.4)) #true

print(bool(0)) #false

print(bool(0.0)) #false

print(bool('')) #false

# and returns the first value that is false
print(1 and 0) #false

print('This' and 'That') #That

print('This' and 0 and 'That') #0

print(0.0 and 1) #0.0

# or returns the first value that is true
print(1 or 0)

print(0 or 1)

print(0 or '')

print(0 or 1 or 'This')

# not will return the opposite value truthy of something
print(not "") #not bool("") => True

print(not 1)