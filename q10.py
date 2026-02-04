import numpy as np

A = np.array([[1, 1], [0, 1], [1, 0]])

U, S, Vh = np.linalg.svd(A, full_matrices = False)

print("\n\n", U)
print("\n\n", S)
print("\n\n", Vh)