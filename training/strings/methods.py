# string methods

str = 'tEsTiNg'
print(str.capitalize()) # Testing
print(str.upper()) # TESTING
print(str.lower()) # testing

str_2 = 'This is a multiword string'
print(str_2.title())

print('Kevin@example.com'.lower() == "kevin@example.com")

# is -> checks for common patterns

# checks if all the characters can be represented by ASCII
print(str.isascii())

print(str.islower()) # false

print(str.islower()) # false

print(str.title().istitle()) # true

print(''.isspace()) # true

'1.0'.isdecimal() # false

# working with strings as tokens
phrase = "This is a simple phrase"

# split phrase into a list of different words
words = phrase.split() 
print(words)

url = "https://example.com/user/jimmy"

# splits on forwards slash and gets the last value of the list
user = url.split('/')[-1]
print(user)

# joining
# use a string that you want to insert in between strings
word_updated = ', '.join(words)
print(word_updated) # This, is, a, simple, phrase

lines = ['first line', 'second line', 'third line']
output = '\n'.join(lines)

print(output)
# first line
# second line
# third line

# format method
# inserting dynamic bits to a string

template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"

# inserts arguments into a tuple and unpacks them in the string
print(template.format('Ricky', 'Napping'))

print("Hello, my name is {0} and I enjoy {1}. Have a nice day. - {0}".format('Ricky', 'Napping'))