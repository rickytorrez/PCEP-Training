my_range = range(10) # takes start, stop and step or just the stop

print(my_range) # range(0,10)

print(list(my_range)) # [1,2,3,4,5,6,7,8,9,10]

print(list(range(1, 14, 2)))

count = 1

while count <= 4:
    print('looping')
    count += 1
    
for _ in range(4):
    print('looping x2')