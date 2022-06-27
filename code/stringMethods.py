print("This".lower())

my_str = 'tEsTiNg'

print(my_str.upper())

print(my_str.capitalize())

print("This is a multiword String".title())

print(my_str.isascii())

print(my_str.islower())

print(my_str.isupper())

print(my_str.istitle())

print('1.0'.isdecimal())

print('1'.isdecimal())

print('1a'.isalpha())

url = 'https://example.com/users/rob'
user = url.split('/')[-1]
print(user)

# substitution groupings
template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
print(template.format('Keith', 'Python'))
