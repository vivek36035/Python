import numpy as np

# Create a 3D array
arr = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                
                [[7, 8, 9],
                 [10, 11, 12]]])

print("3D Array:\n", arr)

print("Shape:", arr.shape)     
print("Dimensions:", arr.ndim)

print("Element from 1st block, 2nd row, 3rd column:", arr[0][1][2])

print("Sum of all elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))
print("Max value:", np.max(arr))

print("First block:\n", arr[0])
print("Second block:\n", arr[1])

reshaped = arr.reshape(4, 3)
print("Reshaped to 2D (4x3):\n", reshaped)