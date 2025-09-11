from array import array

arr = array('i', [1, 2, 3, 4, 5])

arr.append(6)
arr.extend([7, 8])
arr.insert(2, 10)
arr.remove(10)
arr.pop()
print(arr.index(4))
print(arr.count(2))
arr.reverse()
arr2 = array('i', [100, 200])

