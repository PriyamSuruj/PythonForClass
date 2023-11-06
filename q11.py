# Set - Collection of nuremical data
# Set- { }, Mutable, Unordered, Doesn't allow duplicates, Haterogeneus (values having hash table)
set={2,20,30,40}
print(set)
print(len(set))

# Access the item
print(20 in set)
print(50 in set)

# Add item
set.add(100)
print(set)

# Remove item
set.remove(100)
print(set)


s1={20,30,40}
s2={60,70,80}
s1.update(s2)
print(s1)

# Joint operator
# Union
s1={20,30,40}
s2={60,70,80}
s3=s1.union(s2)
print(s3)

# Intersection
s1={20,30,40}
s2={60,30,80}
s3=s1.intersection(s2)
print(s3)

# Dictionary
# It stores the elements in key:value pair.
# {key:value}
# Ordered, Mutable, Doesn't allow duplicates
#Q1 Why we use dictionary 

a={'name':'suruj','age':19,'roll':18}
print(a)
print(len(a))

# Access
print(a['name'])
print(a['age'])

# get()
x=a.get('roll')
print(x)

# changing the item
a['name']='Priyam'
print(a)

# update
a.update({'roll':17})
print(a)

# remove
a.pop('age')
print(a)