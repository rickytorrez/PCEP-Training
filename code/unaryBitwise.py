a = 0b010
print(a)

print(~a) # -a - 1

# ~a = -1 * a - 1

print(bin(~a))

### bitwise

# AND OR XOR NOT
b = 0b1001
c = 0b1100

# or -> if either is true, result is true
print(bin(b | c))

# and -> both to be true or they're false
print(bin(b & c))

#xor -> only one truthy value
print(bin(b ^ c))

# shift -> shift the number to the right by two digits
d = 0b110
print(bin( d >> 2))

print(bin( d << 2))
