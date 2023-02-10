# conditionally do things inside loop to stop execution and either go
# back and into the next iteration or to completely cancel out of a loop

# continue 
# helps move into the next iteration
count = 0

while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}") # else statement
    count +=1

# We're counting odd numbers: 1
# We're counting odd numbers: 3
# We're counting odd numbers: 5
# We're counting odd numbers: 7
# We're counting odd numbers: 9


# break
# stops the execution of the loop entirely
counter = 1

while counter < 10:
    if counter % 2 == 0:
        counter += 1
        break
    print(f"We're counting odd numbers: {counter}") # else statement
    counter +=1
    
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue # skip blue
    elif color == 'red':
        break
    print(color)