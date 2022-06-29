colors = ['red', 'blue', 'orange', 'yellow']
uppercase_colors = []

for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)

# list comprehension
titled_colors = [color.capitalize() for color in colors]
print(titled_colors)

warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)