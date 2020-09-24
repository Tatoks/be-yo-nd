import numpy as np

# 1
list = [15.65, 95, 13, 24.54, 15, 24]
print('Original', list)
l = np.array(list)
print('One dimensional', l)

# 2
arr = np.arange(2, 11)
print("Value Ranging", arr)

# 3
arr1 = np.zeros(10)
arr1[6] = 11
print('Null vector', arr1)

# 4
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([10, 40, 30, 10])
res = arr2 == arr1
print(res)
