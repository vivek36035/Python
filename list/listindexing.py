list1 = ['apple', 'banana', 'cherry']
print("List using []:", list1)

list2 = list((1, 2.34, 'A','c',4))
print("List using list():", list2)

#Positive Indexing
print(list2[0:4])
print(list2[0:])
print(list2[:])
print(list2[:4])
print(list2[0:4:2])

#Negative Indexing

print(list2[-1])
print(list2[-3])
print(list2[-4:-2])
print(list2[-4:])
print(list2[-1:-3])  #empty
print(list2[:-1])