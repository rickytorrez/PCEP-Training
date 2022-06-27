# immutable sequence type, fixed length

point = (2.0, 3.0)
print(point)

point_3d = point + (4.0,) # comma is needed to concat together
print(point_3d)

x, y, z, = point_3d

print(x)
print(y)
print(z)