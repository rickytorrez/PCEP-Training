# go from one type to another

# integer to float
print(float(1))

# float to integer 
# it does not round, it truncates
print(int(1.6))

# cast from number to string
print(str(1))

# convert from string to integer
print(int('1'))

# convert from string to float
print(float('1.0'))

# typecasting for booleans
print(bool(1)) #true
print(bool(2.4)) #true
print(bool('Tada')) #true
print(bool(0)) #false
print(bool(0.0)) #false
# empty versions of strings, dictionaries and lists will be false
print(bool('')) #false

print(1 and 0) #returns first false value

print(1 or 0) #returns the first true value

# empty string is false
print(not "") #returns the opposite value of the object