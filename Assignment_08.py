                                            # 1) Create NumPy arrays  


import numpy as np

# Random values array (shape 4x2)
arr = np.random.rand(4, 2)
print("Random 4x2 array:\n", arr)

# Empty and full array (4x2)
arr2 = np.empty((4, 2))
print("\nEmpty 4x2 array:\n", arr)

arr3 = np.full((4, 2), 7)  # example with value 7
print("\nFull 4x2 array with 7:\n",arr3 )

# Array filled with zeros (3x5)
arr4 = np.zeros((3, 5))
print("\n3x5 array filled with zeros:\n", arr)

# Array filled with ones (4x3x2)
arr5 = np.ones((4, 3, 2))
print("\n4x3x2 array filled with ones:\n", arr5)


                                            #  2) 3x3 matrix with values from 2 to 10


arr6 = np.arange(2, 11).reshape(3, 3)
print("\n3x3 matrix from 2 to 10:\n", arr6)


                                            #  3) Null vector size 10 and update 6th value to 11


null_vector = np.zeros(10)
null_vector[5] = 11
print("\nNull vector with sixth value set to 11:\n", null_vector)


                                            #   4) Reverse an array


arr7 = np.array([10, 20, 30, 40])
reversed= arr7[::-1]
print("\nOriginal array:", arr7,"\n")
print("Reversed array:", reversed,"\n") 


                                             #   5) Convert an array to float type


arr8 = np.array([1, 2, 3, 4])
print("Original array:")
print(arr8,"\n")

# Convert to float type
arr9 = arr.astype(float)
print("Array converted to a float type:","\n")
print(arr9,"\n")

                                               
