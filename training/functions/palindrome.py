def splitName (name):
    firstName, lastName = name.split(maxsplit = 1) # split on the first space
    # firstName = names[0]
    # lastName = names[-1]
    return {
        'first_name': firstName,
        'last_name': lastName
    }
        
print(splitName('Ricky Torrez'))

# use slicing to reverse a string
def isPalindrome (item):
    item = str(item)
    return item == item[::-1]
    
print(isPalindrome('tacocat'))
print(isPalindrome('8118'))

# include an item repated by the number of times parameter
def buildList (item, count = 1):
    numbr = 1
    items = []
    while numbr <= count:
        items.append(item)
        numbr += 1
    return items
    
    # for _ in range(count):
    #     items.append(item)
    # return items

print(buildList('Apple', 3))