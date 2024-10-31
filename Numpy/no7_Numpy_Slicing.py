import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr[0:5])
# print(arr[-1])

multi_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multi_arr)

# print(multi_arr[1, 2])  # from row-1 return element-2
# print(multi_arr[-1])
# print(multi_arr[-1, 0:2])
print(multi_arr[:, 1:3])
