import numpy as np

W = np.array([[0.2, 0.4, 0.1],
              [0.5, 0.1, 0.3]])

x = np.array([10, 20, 30])
b = np.array([1, 1])

z = W @ x + b

print("Saída z =")
print(z)
