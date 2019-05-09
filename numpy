import numpy as np

A = np.array([2, 4, 6, 8, 10])
print(A)
print("A=", type(A))
print("A.ndim=", A.ndim) #一維陣列
print("A.shape=", A.shape) 
print("A.size=", A.size) #個數
print("A.dtype=", A.dtype) #預設資料型態

#-------------

import numpy as np

A = np.array([2, 4, 6, 8, 10])
A[2]=100
print(A)
B = np.insert(A, 2, 99)
print(B)
C = np.insert(B, [1, 4], 0)
print(C)
D = np.delete(C, 4)
print(D)
E = np.array([-1, -1])
print(np.concatenate((D, E)))

#-------------

import numpy as np

A = np.array([1, 2, 3])
B = np.array([1, 0, 1])
print("內積:", np.inner(A, B))
print("叉積:", np.cross(A, B))
print("外積:", np.outer(A, B))
