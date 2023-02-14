# parameter -> variables defined when defining the function itself
# values used within function
# IE: name, age, car_model

def contactCard (name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

# argument -> value provided (passed) for name, age, car_model when the function is used
# they exist at the time of calling the function

print(contactCard('Keith', 29, 'Honda Civic'))
# passing args in different positions with key names
print(contactCard(age=39, car_model='Ford F150', name='Robert'))
# once a keyword arg is defined, they (keywords) must be used after
print(contactCard('Paolo', car_model='Prius', age='37'))

def canDrive (age, drivingAge = 16):
    return age >= drivingAge
    
print(canDrive(29))
print(canDrive(16, 18))

# default args (16) must be follow by another default argument
def can_drive (age, driving_age = 16, vehicle_type='Honda'):
    pass