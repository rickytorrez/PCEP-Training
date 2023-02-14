# never name hide

y = 5

def setAbc (y):
    print('Inner Y: ', y)
    x = y
    y = x
    
setAbc(10) # 10, argument passed to function

print('Outer y: ', y) # 5, parameter is higher than an argument, higher context variable