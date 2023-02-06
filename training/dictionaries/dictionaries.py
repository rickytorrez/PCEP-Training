# dictionaries

# keys have to be immutable types and must be unique
ages = { 'kevin': 59, 'alex': 29, 'bob': 40}
print(ages)

# reading values for a specific key
print(ages['kevin'])

# adding values
ages['kayla'] = 21
print(ages)

# reassigning values
ages['kevin'] = 60
print(ages)

# remove a value - delete the key
del ages['kevin']
print(ages)

# checking for existence
print('kevin' in ages) # false
print('alex' in ages) # true

# creating dictionaries

# dict function
weights = dict(kevin= 160, bob= 240, kayla=135)

# using tuples
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla','red')])
