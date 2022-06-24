test_str = 'testing'
print(test_str[0]) # does not modify original string but returns a new one

print(test_str[len(test_str) -1]) # gets last character from string => g
print(test_str[-1]) # last item -> g
print(test_str[-4]) # 4 items from last to first -> t

# slicing allows us to specify ranges of indexes to work with
# 0 -> index you want to start with
# 2 -> index that is just outside of the item we want
print(test_str[0:2]) # 'te'
print(test_str[3:5]) # 'ti'
print(test_str[2:len(test_str)]) # 'sting'

# from index of 2 all the way to the end of the string
print(test_str[2:]) # 'sting'

# stepping by 2 by adding a third argument :2
# 5 is outside the range
print(test_str[1:5:2]) # 'et'

# start index
# end index
# step value
print(test_str[1:6:2]) # 'etn'

print(test_str[::-1]) # 'gnistset'

