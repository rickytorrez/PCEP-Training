# change binary representation right or left

a = 0b110

# shifts number to the right two digits and drops the shifted digits
print(bin(a >> 2))

# shifts number four digits, returns a zero
print(bin(a >> 4))

# adds zeros (pads) to the end 0b11000
print(bin(a << 2))