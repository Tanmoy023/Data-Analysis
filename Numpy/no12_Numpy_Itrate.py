import numpy as np

a = np.arange(12).reshape(3, 4)
# print(a)

# for x in np.nditer(a, order="C"):  # print elements row-by-row
#     print(x)

# for x in np.nditer(a, order="F"): # print elements colum-by-colum
#     print(x)

# for x in np.nditer(a, order="F", flags=["external_loop"]):  # print column one-by-one
#     print(x)

# keep read-and-write operation in original numpy array
for x in np.nditer(a, op_flags=["readwrite"]):
    x[...] = x * x
print(a)

b = np.arange(3, 15, 4).reshape(3, 1)
print(b)

for x, y in np.nditer([a, b]):
    print(x, y)
