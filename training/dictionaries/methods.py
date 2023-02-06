#dictionary methods
ages = {'kevin': 61, 'bob': 79}

# get the keys by using the following method
print(ages.keys()) # returns a dict object with keys

# to turn into a list, we'll need to cast
ages_list = list(ages.keys())
print(ages_list)

# values
print(ages.values())
ages_values = list(ages.values())
print(ages_values)

# items -> returns key and values
print(ages.items())
ages_items = list(ages.items())
print(ages_items)