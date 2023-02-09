# more common type of loop

# general structure of loops
# for TEMP_VARIABLE in SEQUENCE (list, tuple, string):
#     print(TEMP_VARIABLE)

# iterating through a list
colors = ['blue', 'green', 'red', 'purple']

for color in colors:
    print(color)
# blue
# green
# red
# purple

# iterating through a tuple
point = (1, 2, 3)

for value in point:
    print(value)
    
# iterating through dictionaries
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}

# for the key only
for key in ages:
    print(key)
    
# for the value, unpack all the info
for key, value in ages.items():
    print(key, value)
    
# iterating through a string
str = 'my string'

for letter in str:
    print(letter)