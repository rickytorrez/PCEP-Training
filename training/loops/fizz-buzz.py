number = int(input('Please provide a number from 1-30: ' ))

for _ in range(1, number + 1):
    if _ % 3 == 0 and _ % 5 == 0:
        print('fizz-buzz')
    elif _ % 3 == 0:
        print('fizz')
    elif _ % 5 == 0:
        print('buzz')
    else:
        print(_)