# Original dictionary
d = {'name': 'Vivek', 'age': 21, 'city': 'Pune'}

# 1. get()
print("get('name'):", d.get('name'))
print("get('country', 'India'):", d.get('country', 'India'))

# 2. keys()
print("keys():", d.keys())

# 3. values()
print("values():", d.values())

# 4. items()
print("items():", d.items())

# 5. copy()
d_copy = d.copy()
print("copy():", d_copy)

# 7. setdefault()
d.setdefault('country', 'India')
print("setdefault():", d)

# 8. pop()
age = d.pop('age')
print("pop('age'):", age)
print("After pop:", d)

# 9. popitem()
last_item = d.popitem()
print("popitem():", last_item)
print("After popitem:", d)

# 10. update()
d.update({'email': 'vivek@example.com'})
print("update():", d)

# 11. clear()
d.clear()
print("clear():", d)  # {}
