import numpy as np

# Create an 1D numpy array with 10 zeros.
print(np.zeros(10))
# Create a 2D np array with 10 zeros, shaped (5,5)
print(np.zeros((5,5)))


# Using arange OR linspace functions...
# Make an array with 0.5 evenly spaced values from 0 (inclusive) to 1.05 (exclusive)
print(np.arange(0, 1+0.5, 0.5))
print(np.linspace(0, 1, 3))


# Indexing  & Slicing
pythonn = np.arange(10)**3
print(pythonn)
# print the element at index 2 of the array 'pythonn'
print(pythonn[2])
# print the elements at indices 3 to 5 of the array
print(pythonn[3:6])


# Boolean
# Print only the elements that are greater than or equal to 64 from the array 'pythonn'
pythonn_64 = pythonn >= 64
print(pythonn[pythonn_64])


# Stacking & Splitting
pythonn_1 = np.array([1, 2, 3, 4, 5, 6]).reshape(2,3)
pythonn_2 = np.array([7, 8, 9, 10, 11, 12]).reshape(2,3)
# Vertically stack pythonn_1 and pythonn_2 and print them
print(np.vstack((pythonn_1, pythonn_2)))
# Horizontally stack the two arrays
print(np.hstack((pythonn_1, pythonn_2)))
# Split the pythonn_1 array into 3 equal parts along the columns
print(np.hsplit(pythonn_1, 3))
#Split the pythonn_1 array into 2 equal parts along the rows
print(np.vsplit(pythonn_1, 2))


# END

