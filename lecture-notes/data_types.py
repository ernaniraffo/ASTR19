'''Test data types in numpy'''

import numpy as np

# np.int64
A = np.zeros(10, dtype=int)
print("A:", A)
print("type(A):", type(A))
print("type(A[0]):", type(A[0]))

# floats
X = 19.10
print("X:", X)
print("type(X):", type(X))

# e is equivalent to *10^(...)
Y = 1.9e2 # 1.9*10^(2) = 190.0
print("Y:", Y)
print("type(Y):", type(Y))

# np.float64
Z = np.zeros(10, dtype=float)
print("Z:", Z)
print("type(Z):", type(Z))
print("type(Z[0]):", type(Z[0]))
