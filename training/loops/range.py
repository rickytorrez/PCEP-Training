# range -> for when we iterate a certain number of times
# immutable sequence type

# takes a start, stop and a step
# lightweight, only count when it's needed
# or simply a number -> stop value
my_range = range(10)
print(my_range) # range(0, 10)

print(list(my_range)) # [0,1,2,3,4,5,6,7,8,9]

print(list(range(1, 14, 2))) # [1,3,5,7,9,11,13]

# while loop
count = 1

while count <= 4:
    print('looping', count)
    count += 1

# underscore is used when we don't care for the variable
for _ in range(4):
    print('looping', _)