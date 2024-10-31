import numpy as np

multi_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(multi_arr)

for row in multi_arr:
    print(row)

for cell in multi_arr.flat:
    print(cell)
