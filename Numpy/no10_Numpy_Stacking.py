import numpy as np

a = np.arange(6).reshape(3, 2)
# print(a)
b = np.arange(6, 12).reshape(3, 2)
# print(b)

vstack = np.vstack((a, b))  # vertically stack a and b
print(vstack)

hstack = np.hstack((a, b))
print(hstack)
