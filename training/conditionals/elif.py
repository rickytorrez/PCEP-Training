# elif -> helps us handle multiple cases 
# for many branches of logic
# used in the middle of if/else

# if 'b' < 'a':
#     print('this is true')
# elif 'c' < 'd':
#     print('second condition is true')
# else:
#     print('no condition was true')

name = input('What is your name? ')

if len(name) >= 6:
    print('Your name is long')
elif len(name) == 5:
    print('Your name is five chars long')
elif len(name) >= 4:
    print('Your name is four chars long')
else:
    print('Your name is short.')