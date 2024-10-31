import numpy as np

arr = np.arange(30).reshape(2, 15)

hsplit = np.hsplit(arr, 3)
# print(hsplit[0])
# print(hsplit[1])
# print(hsplit[2])

vsplit = np.vsplit(arr, 2)
print(vsplit[0])
print(vsplit[1])
