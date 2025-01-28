import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])

# Slice the first array (1D)
# For example, let's slice from index 1 to 4 (excluding 4)
slice1 = array1[1:4]

# Slice the second array (2D)
# For example, let's slice the first two rows and the first two columns
slice2 = array2[:2, :2]

print("Original array1:", array1)
print("Sliced array1:", slice1)

print("Original array2:")
print(array2)
print("Sliced array2:")
print(slice2)
