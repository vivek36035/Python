a = {1, 2, 3}
b = set([3, 4, 5])
print("Set a:", a)
print("Set b:", b)

# add()
print("\nadd():")
a.add(10)
print("After a.add(10):", a)

# update()
print("\nupdate():")
a.update([20, 30])
print("After a.update([20, 30]):", a)

# remove()
print("\nremove():")
a.remove(10)
print("After a.remove(10):", a)
# a.remove(99)  # KeyError if uncommented

# discard()
print("\ndiscard():")
a.discard(20)
a.discard(99)  # No error if not found
print("After a.discard(20) and a.discard(99):", a)

# pop()
print("\npop():")
popped = a.pop()
print("Popped element:", popped)
print("Set after pop():", a)

# clear()
print("\nclear():")
temp = a.copy()
temp.clear()
print("After clear():", temp)

# copy()
print("\ncopy():")

copy_set = b.copy()
print("Copied set:", copy_set)

# union()
print("\nunion():")
print("a | b =", a.union(b))

# intersection()
print("\nintersection():")
print("a & b =", a.intersection(b))

# difference()
print("\ndifference():")
print("a - b =", a.difference(b))

# symmetric_difference()
print("\nsymmetric_difference():")
print("a ^ b =", a.symmetric_difference(b))

# issubset()
print("\nissubset():")
print("{3}.issubset(b):", {3}.issubset(b))

# issuperset()
print("\nissuperset():")
print("b.issuperset({3}):", b.issuperset({3}))

# isdisjoint()
print("\nisdisjoint():")
print("a.isdisjoint({100, 200}):", a.isdisjoint({100, 200}))
print("a.isdisjoint(b):", a.isdisjoint(b))
