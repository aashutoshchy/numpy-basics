import numpy as np

# print(np.__version__) # checking numpy version


# very basics
# array = np.array([1,2,3,4])

# array = array * 2

# print(array)

# array = np.array(['A', 'B', 'C']) # 1D array
array = np.array([['A', 'B', 'C'],
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I']]) # 2D array
print(array.ndim)
print(array.shape)


# Accessing elements through Multidimensional indexing
print(array[0, 1]) # prints 'B'
