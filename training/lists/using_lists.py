users = []

users.append('kevin')
users.append('bob')
users.append('alice')
print(users)

users.remove('bob')
print(users)

rev_users = list(reversed(users))
print(rev_users)

rev_users.insert(1, 'melody')
print(rev_users)

rev_users += ['andy', 'wanda', 'jim']
print(rev_users)

center_users = rev_users[1:3]
print(center_users)