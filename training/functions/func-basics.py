# functions -> group chuncks of code together into reusable blocks

# structure
# def functionName(some_parameter, other_parameter):
#    body of our function goes here

def print_name(name):
    print(f"Name is {name}")
    
print_name('Ricky')


def add_two(num):
    return num + 2
    
result = add_two(2)
print(result)

# multiple parameters
def add(num1, num2):
    return num1 + num2

print(add(1,5))
print(add(17,38))