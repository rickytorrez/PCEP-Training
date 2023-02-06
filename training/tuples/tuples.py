# tuple -> immutable sequence type
# a point to graph something out is a good example
# cannot modify a point, cannot change size
point = (2.0, 3.0)
print(point)

# to create a 3d point
# comma is added to avoid order of operations
# comma helps concatenate 
point_3d = point + (4.0,)
print(point_3d)

# to separate a point into its own variables
x, y, z = point_3d

print(x)
print(y)
print(z)

# real life example
print("My name is: %s %s" % ("Ricky", "Torrez"))
