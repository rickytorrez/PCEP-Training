ages = { 'kevin': 61, 'bob': 79}
keys = ages.keys()
print(keys) # dict_keys(['kevin', 'bob'])

formatted_keys = list(ages.keys())
print(formatted_keys)

vals = ages.values()
print(list(ages.values()))

# items gives us a list of tuples with key value pairs
items = ages.items()
print(list(items))