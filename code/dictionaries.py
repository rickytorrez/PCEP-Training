ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages)

# subscribing
print(ages['kevin'])

# adding to the dictionary
ages['kayla'] = 21
print(ages)

# re-assign values
ages['kevin'] = 60
print(ages)

# deleting values
del ages['kevin']
print(ages)

print('kevin' in ages) # check for the key value kevin in the ages dict
print('alex' in ages)

# creating dictionaries
weights = dict(kevin=160, bob=240, kayla=135)
print(weights)

colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)