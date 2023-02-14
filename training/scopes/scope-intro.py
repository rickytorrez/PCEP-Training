# how scopes work

# conditionals and loops do not define their own scopes
if 1 < 2:
    x = 5
    
while x < 6:
    print(x)
    x += 1

print(x)


# functions and classes define their own scope
# variables created inside of a function remain inside of the function
def setY():
    y = 5
    
setY()

# while y < 3:
#     print(y)
#     y += 1