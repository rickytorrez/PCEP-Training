# list comprehension ->
# sequence (list), go through each item and make a modification
# and end up with a list

# formatting values and adding to a list
colors = ['red', 'orange', 'blue', 'green', 'yellow']

uppercase_colors = []

# for color in colors:
#     uppercase_colors.append(color.upper())


# take the list, put a for loop inside of a list and write a sentence of what we want done

# [what we yield for the particular iteration (be processed in this way), iteration]
uppercase_colors = [color.upper() for color in colors]

print(uppercase_colors)

# filtering values to add to a list
# warm_colors = []

# for color in colors:
#     if color in ['red', 'orange', 'yellow']:
#         warm_colors.append(color)
        
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]

print(warm_colors)