import numpy as np
import time
import sys

list = [1] * 1000  # crate a list with 1000 elements
print("size of this list is : ", sys.getsizeof(1) * len(list))
# sys.getsizeof(1) is size of a single integer element in byte

NpArr = np.arange(1000)
print("type of a numpy array : ", type(NpArr))
print(f"size of this npArr : ", NpArr.size * NpArr.itemsize)
# NpArr.size is total length of an array.    NpArr.itemsize is size of a single numpy array element
