# unary operators

a = 0b010
print(a)

## formula -> -a -1
## -1 * a - 1
print(~a) # -3

# boolean operators
# AND OR XOR NOT

b = 0b1001
c = 0b1100

# bitwise OR operator => |
# will print whichever bit is true from both variables 
print(b | c)
print(bin(b | c)) #0b1101

# bitwise AND operator => &
# will only show which bite is true on both variables
print(bin(b & c)) #0b1000

# bitwise XOR (exclusive or) operator => ^
# you can only have one truthy value between the two things you're comparing
print(bin(b ^ c))