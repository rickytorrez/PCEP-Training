number = int(input('Please provide a number: '))

if number % 5 == 0 and number % 3 == 0:
    print('fizzbuzz')
elif number % 3 == 0:
    print('fizz')
elif number % 5 == 0:
    print('buzz')
else:
    print(number)