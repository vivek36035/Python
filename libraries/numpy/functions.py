import numpy as np

# 1 np.array()
arr = np.array([1,2,3,4])
print(arr)

#2 np.arange()
arr = np.arange(0,10,2)
print(arr)

#3 np.zeroes,np.ones
zeros = np.zeros((2,3))
ones = np.ones((2,3))
print(zeros)
print(ones) 

#4 np.random.rand(),np.random.randit()
rand = np.random.rand(2,3)
rand_int = np.random.randint(1,10,size=(3,3))
print(rand)
print(rand_int)

#5np.reshape()
arr = np.arange(6)
reshaped = arr.reshape(2,3)
print(reshaped)

#6 np.sum()/np.mean().np.max(),np.min()
arr = np.array([1,2,3,4])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

#7np.dot()/np.matmul()
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a,b))

#8 np.transpose()
a = np.array([[1,2],[3,4]])
print(np.transpose(a))

#9np.where()
arr = np.array([10,20,30,40,50])
result = np.where(arr>20)
print(result)

#10np.linspace()
arr = np.linspace(0,1,5)
print(arr)