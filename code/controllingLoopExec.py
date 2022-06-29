# continue stops execution of loop for current iteration
count = 0

while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1
    
# break stops the execution enterely - no longer loops at all
count = 1
while count < 20:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
 
# only red gets printed  
colors = ['blue', 'red', 'green', 'purple']

for color in colors:
    if color == 'blue':
        continue
    elif color == 'green':
        break
    print(color)