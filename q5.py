import numpy as np

A = np.array([[1, 2],
              [3, 4]])

det = np.linalg.det(A)
print(f"Determinante: {det:g}")

if det != 0:
    A_inv = np.linalg.inv(A)
    print("Matriz inversa:")
    print(A_inv)
else:
    print("A matriz não é invertível.")
