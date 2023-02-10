# recursion
# when defining a function, we can call that function within itself

# fibb sequnce [1,1,2,3,5,8,13,21]

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 2) + fib (n - 1)
    
item_to_calculate = int(input('What fib item would you like to calculate: '))
print(fib(item_to_calculate))