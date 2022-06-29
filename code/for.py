# looping - for

# for TEMP_VARIABLE in SEQUENCE:
#   pass

#list
colors = ['blue', 'green', 'red', 'purple']

for color in colors:
    print(color)

# tuple
point = (1, 2, 3)

for value in point:
    print(value)

# dictionary
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}

for key in ages:
    print(key)
    
for key, value in ages.items():
    print(key, value)
    
# string
for letter in 'my_string':
    print(letter)
