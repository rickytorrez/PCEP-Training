# Create a list of services using Python. IE: S3, Lambda, EC2, etc

# 1. The list should be empty initially.
services = []

# 2. Populate the list using append or insert.
services.append('s3')
services.append('ec2')
services.append('dynamodb')
services.append('cloudformation')
services.append('lambda')

# 3. Print the list and the length of the list.
print(services)
print('Number of services in list', len(services))

# 4. Remove two specific services from the list by name or by index.
services.remove('lambda')
del services[3]

# 5. Print the new list and the new length of the list.
print(services)
print('Number of services in list', len(services))