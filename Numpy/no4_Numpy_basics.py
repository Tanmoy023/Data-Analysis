import numpy as np

zeros = np.zeros((3, 4))  # np.zeros((shape)) it crate a 2-by-3 numpy array with all 0
print(zeros)

ones = np.ones((4, 5))
print(ones)

arr_arange = np.arange(1, 10)  # create a numpy array form 1 to 10-1
print(arr_arange)

arr_arange_gap = np.arange(1, 10, 2)
# create a numpy array form 1 to 10-1 with 2 number of gap
print(arr_arange_gap)

arr_linspace = np.linspace(1, 5, 10)
# create a numpy array with linearly spaced 10 elements between 1 to 5
print(arr_linspace)
