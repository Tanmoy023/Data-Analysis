import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)

bool_array = arr < 6
print(bool_array)

true_array = arr[bool_array]
print(true_array)


arr[bool_array] = -1
print(arr)
