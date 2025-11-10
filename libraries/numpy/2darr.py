import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("2D Array:\n", arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

print("Element at row 1, column 2:", arr[0][1])

print("Sum of all elements:", np.sum(arr))
print("Row-wise sum:", np.sum(arr, axis=1))
print("Column-wise sum:", np.sum(arr, axis=0))

print("Transpose:\n", np.transpose(arr))

result = np.dot(arr, arr)
print("Matrix multiplication result:\n", result)
