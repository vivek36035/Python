import array

a = array.array('b', [1, -2, 3])
print("b:", a)

a = array.array('B', [1, 2, 255])
print("B:", a)

a = array.array('u', 'hello')
print("u:", a)

a = array.array('h', [1000, -2000])
print("h:", a)

a = array.array('H', [1000, 65000])
print("H:", a)

a = array.array('i', [10, -20, 30])
print("i:", a)

a = array.array('I', [10, 20, 40000])
print("I:", a)

a = array.array('l', [100000, -200000])
print("l:", a)

a = array.array('L', [100000, 200000])
print("L:", a)

a = array.array('q', [1000000000, -2000000000])
print("q:", a)

a = array.array('Q', [1000000000, 2000000000])
print("Q:", a)

a = array.array('f', [1.5, 2.3, -3.9])
print("f:", a)

a = array.array('d', [1.23456789, -9.87654321])
print("d:", a)
