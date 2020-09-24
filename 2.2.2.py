import np as np
import numpy as np
from numpy.linalg import inv

# 1 Write a NumPy program to compute the multiplication of two given matrixes
x = [[1, 2], [5, 6]]
y = [[4, 5], [9, 5]]
print("original:")
print(x)
print(y)
result = np.dot(x, y)
print("Multiplication:")
print(result, "\n")

# 2Write a NumPy program to compute the determinant of an array
x = np.array([[1, 2], [3, 4]])
print("original arr:")
print(x)
result = np.linalg.det(x)
print("determinant:")
print(result, '\n')

# 3 Write a NumPy program to compute the sum of the diagonal element of a given array
x = np.array([[2, 4, 5], [8, 9, 10], [12, 15, 16]])
print(x, "matrix:")
diag = np.diagonal(x)
print("\nDiagonal matrix:")
print(diag)
print("\nSum of diagonal matrix:")
print(sum(diag))

# 4Write a NumPy program to compute the inverse of a given matrix
x = np.array([[1, 2], [3, 4]])
print("original matrix:")
print(x)
result = np.linalg.inv(x)
print("inverse matrix:")
print(result, "\n")

#5Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
x = np.arange(15)
np.save('another_x', x)
read_file_info = np.load('another_x.npy')
print(read_file_info)
