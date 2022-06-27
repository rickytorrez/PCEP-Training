num = int(input('Enter an integer value: '))

if num % 5 == 0 and num % 3 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)