count = 1

while count <= 4:
    print(count)
    count += 1
else:
    print('while loop completed')

for i in [1,2,3,4,5]:
    print(i)
else: 
    print('for loop completed')
    
colors = ['red', 'pink', 'blue', 'orange', 'green']

for color in colors:
    if color == 'orange':
        print('orange is in the list')
        break
else: 
    print('orange is not in the list')