# text based, collection of characters

# strings are created with 'single' or "double quotes"

# we can also do multi line strings
'''
Multi line string
'''


str = 'pass' + 'word'
print(str)

# errors out, unsupported operand
# str1 = 'pass' - 'word'

str2 = 'Ha' * 4
print(str2)

# a string is known as an object in python
# it encapsulates state (sequence of characters)
# and behavior (functionality that is tied to this content)

# state 
str3 = "my_string"

# behavior is represented by a method
# we access methods on objects by chaining them using a period
print(str3.find('t'))
print(str3.find('in'))
print(str3.upper())

tab = "Tab\tDelimited"
print(tab)

new_line = "New\nLine"
print(new_line)

singles = "'Single' in Double"
print(singles)

doubles = '"Doubles" in Single'
print(doubles)

doub_on_doub = "\"Double\" in Doubles"
print(doub_on_doub)