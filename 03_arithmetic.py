import numpy as np

# Scalaer arithmetic

# array = np.array([1,2,3])

# print(array + 1)
# print(array - 1)
# print(array * 1)
# print(array / 2)
# print(array ** 2)

# Vectorized math funcs

# array = np.array([1.02, 2.56, 3.12])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(np.pi))

# Exercise

# radii = np.array([1, 2, 3])

# print(np.pi * radii ** 2)

# Element-wise arithmetic
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(arr1 + arr2)
# print(arr1 * arr2)

# Comparison operators

scores = np.array([91, 12, 52, 45, 100, 67, 31])

# print(scores >= 30)

scores[scores < 40] = 0
print(scores)

