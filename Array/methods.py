#append

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#copy
x = fruits.copy()
print(x)

#count
y = fruits.count("cherry")
print(y)

#extend()
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#index()
z = fruits.index("cherry")
print(z)

#insert()
fruits.insert(1, "orange")
print(fruits)

#reverse()
fruits.reverse()
print(fruits)

#sort()
cars.sort()
print(cars)

#clear()
fruits.clear()
print(fruits)