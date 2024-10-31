import numpy as np
import time
import sys

size = 1000000

l1 = [1] * size
l2 = range(size)  # create a object which completely similar to list

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
# list comprehension. work like result[i] = l1[i] + l2[i]
print(f"Python list took : {(time.time()-start)*1000}")

start = time.time()
result = a1 + a2
# addition of numpy array. Similar to list comprehension. Other operation is also applicable same way
print(f"Numpy array took : {(time.time()-start)*1000}")
