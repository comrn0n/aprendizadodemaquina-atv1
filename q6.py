import numpy as np

A = np.array([[4, 2], [1, 3]])
r = np.linalg.eig(A)

print("Os autovalores da matriz A são:", r[0])
print("Os autovetores da matriz A são:", r[1])