# turning generator functions into lists

def genRange (stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
        
# casting to a list
# 1st. add the generator object to a variable
# generator = genRange(10)

# 2nd. cast it to a list
# list(generator)
# [1,2,3,4,5,6,7,8,9,10]


def geb_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a