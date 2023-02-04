# indexing -> interact with individual items in a string

test_str = "testing"
print(test_str[0]) # t
print(test_str[len(test_str) - 1]) # g
print(test_str[-1]) # g -> -1 is the last item

# slicing -> looking at sub sections of a string
# specifies ranges of indexes to work with

# 0 is the first item being returned and 2 is the stopping index
# 2 does not get included
print(test_str[0:2]) # te
print(test_str[3:5]) # ti

# up until the end of the string
print(test_str[2:len(test_str)]) # sting

# since we won't know the last index for a string, we leave it blank to include remaining characters
print(test_str[2:]) # sting

# starts at index one and ends on index 5, steps by 2 and returns those values
print(test_str[1:5:2]) # et

print(test_str[1:6:2]) # etn

print(test_str[:6:2]) # tsi

# from a specific point all the way to the end
print(test_str[1::2]) # etn

# slice with negative step values, reverses the value
print(test_str[::-1]) # gnitset

