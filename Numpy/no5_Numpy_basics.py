# define axis of a 2 dimention array
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)
print(arr.shape)

reshape = arr.reshape(2, 3)
print(reshape)

ravel = arr.ravel()  # reshape into 1 dimention
print(ravel)

sqrt = np.sqrt(arr)
print(sqrt)

print(np.std(arr))

# print(arr.min())
# print(arr.max())
# print(arr.sum())  # return sum of all elemets
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
