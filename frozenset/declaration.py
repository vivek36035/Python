A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# union
union_set = A.union(B)
print(union_set) 

difference_set = A.difference(B)
print(difference_set) 

# intersection
intersection_set = A.intersection(B)
print(intersection_set)  

# copy
C = A.copy()
print(C)  

# isdisjoint() method
print(A.isdisjoint(C))

# issubset() method
print(C.issubset(B)) 

# issuperset() method
print(B.issuperset(C))