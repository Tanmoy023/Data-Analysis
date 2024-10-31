import numpy as np

arr_1D = np.array([1, 2, 3])  # create 1D numpy array
print(f"arr_1D dimention : {arr_1D.ndim}")
print("Total number of elements in arr_1D is : ", arr_1D.size)
print("(row, column) in arr_1D : ", arr_1D.shape)

arr_2D = np.array([[1, 2], [3, 4], [5, 6]])
print(f"arr_2D dimention : {arr_2D.ndim}")

arr_3D = np.array([[[1], [2]], [[3], [4]]])
print(f"arr_3D dimention : {arr_3D.ndim}")

print(f"arr_1D datatype : {arr_1D.dtype}")
print(f"size of each element of arr_1D : {arr_1D.itemsize} byte")

arr_Change_dt = np.array([1, 2, 3], dtype=np.float64)
print(f"arr_Change_dt datatype : {arr_Change_dt.dtype}")
print(f"size of each element of arr_Change_dt : {arr_Change_dt.itemsize} byte")
