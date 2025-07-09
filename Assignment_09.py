import numpy as np

# 1) Combining a one and a two-dimensional NumPy Array

arr1 = np.array([11, 22, 33])
arr2 = np.array([[44, 55, 66], [77, 88, 99]])
arr1_reshape = arr1[np.newaxis, :]  # Convert to 2D: shape becomes (1, 3)
com = np.concatenate((arr1_reshape, arr2), axis=0)
print("Combination:\n", com, "\n")


# 2) Flatten a 2d numpy array into 1d array (By flatten key and by reshaping)

arr3=np.array([[7,8,9,10],[5,4,3,2]])
a =arr3.reshape(-1)
'''flat=arr3.flatten()'''   
print("2D to 1D Flattening \n:",a,"\n")


# 3) Reverse a numpy array

arr4=np.array([[[1,3,0],[0,2,2],[0,0,5]]])
print("Original Arr4 \n:",arr4)
reverse = arr4[:,:,::-1]
print("Reversed Array: \n",reverse,"\n")


# 4) Practice operations like

# Get the maximum value from given array
arr = np.array([3, 7, 2, 9, 1])
max = np.max(arr)
print("Maximum value :\n", max,"\n")

# Get the minimum value from given array
min = np.min(arr)
print("Minimum value :\n", min,"\n")

# Find the number of rows and columns of a given array using NumPy
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
rows, cols = arr5.shape
print(" Number of rows and columns \n", "Rows:", rows, "Columns:", cols,"\n")

# Select the elements from a given array (each element and specific element)
print("Select the elements :","\n")
for element in arr5.flat:
    print(element, end=' ')
print("Specific element at [1,2]:", arr5[1, 2],"\n")

# Find the sum of values in a 2D array using for loop
total = 0
for row in arr5:
    for val in row:
        total += val
print("Sum of values in a 2D array using for loop\n", total,"\n")

# Adding, Subtracting, multiplying, dividing arrays in Numpy
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("\nAdding:", np.add(a, b))
print("Subtracting:", np.subtract(a, b))
print("Multiplying:", np.multiply(a, b))
print("Dividing:", np.divide(a, b))
