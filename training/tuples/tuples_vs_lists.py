# tuples can't change sizes
# lists can

# tuple
# a person always contains three pieces of info
person = ('Kevin Bacon', 61, "555-555-5555")
person2 = ('Bob Ross', 76, "")
print(person[0])
print(person2[0])

# list on a tuple
my_list = [1,2,3]
my_tuple = (my_list, 1)
print(my_tuple)

# embedding works fine
other_list = [1,2, my_tuple]
print(other_list)

my_list.append(1)
print(my_tuple)