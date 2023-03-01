import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print("\n\nOriginal Array")
print(arr)
print("Array Dimension => ",arr.ndim)
print("Array Shape => ",arr.shape)

print("\n\nFlattend Array")
print(newarr)
print("Array Dimension => ",arr.ndim)
print("Array Shape => ",arr.shape)