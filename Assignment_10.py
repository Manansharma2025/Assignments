import numpy as np
import matplotlib.pyplot as plt

# 1. Replace NaN with 0 and Interchange 3 rows and 3 columns of 2D array

arr1 = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr1 = np.nan_to_num(arr1, nan=0)
arr1_transposed = arr1.T
print("Cleaned Array:\n", arr1)
print("Transposed Array:\n", arr1_transposed,"\n")


# 2. Move axes of 3D array to new positions

arr2 = np.arange(24).reshape(2, 3, 4)
moved_arr2 = np.moveaxis(arr2, 0, -1)
print("Original shape:", arr2.shape)
print("New shape after moving axes:", moved_arr2.shape,"\n")


# 3. Replace NaN values with average of columns

arr3 = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
col_mean3 = np.nanmean(arr3, axis=0)
inds3 = np.where(np.isnan(arr3))
arr3[inds3] = np.take(col_mean3, inds3[1])
print("Array after replacing NaN:\n", arr3,"\n")


# 4. Replace negative value with zero
print("\n4. Replace negative values with zero")
arr4 = np.array([[4, -3, 5], [-1, 9, -8]])
arr4[arr4 < 0] = 0
print("Updated Array:\n", arr4,"\n")


# 5 & 6. Study and import numpy arrays

a1 = np.array([3, 4])
a2 = np.array([1, 0])
avg = (a1 + a2) / 2
print("Average of arrays:\n", avg,"\n")


#7. Average, Mean, Median, Mode of 2D arrays 

arr1 = np.array([[10, 20], [30, 40]])
arr2 = np.array([[5, 15], [25, 35]])

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

mean_val = np.mean(combined)
median_val = np.median(combined)

unique_vals, counts = np.unique(combined, return_counts=True)
max_count = np.max(counts)
modes = unique_vals[counts == max_count]
mode_val = modes[0]

print("Combined Array:\n", combined,"\n")
print("Mean:\n", mean_val,"\n")
print("Median:\n", median_val,"\n")
print("Mode:\n", mode_val,"\n")


# 8. Solve linear equations using linalg() and inverse method

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])

B = np.array([9, -6, 17])

solution = np.linalg.solve(A, B)
print("Solved Eqution: \n", solution,"\n")

A_inv = np.linalg.inv(A)
solution_inv = A_inv @ B
print("Solution using inverse matrix method: \n", solution_inv,"\n")



# 9. Plot semester result comparison
semesters = ['Semester 1', 'Semester 2']
marks = [78, 85]

plt.figure(figsize=(6, 4))
plt.bar(semesters, marks, color=['skyblue', 'orange'])
plt.title("Semester Result Comparison")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
