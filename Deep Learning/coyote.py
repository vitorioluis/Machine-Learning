import numpy as np

# 2 matriz 2x2
A = np.array([[1, 2], [3, 4],])
B = np.array([[5, 6], [7, 8]])


#Multiplicador de matriz
# C = A*B
C = np.dot(A,B)
print(C)


m = A.shape
print(m)