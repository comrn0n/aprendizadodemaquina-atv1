import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

covariancia = np.cov(x)

print("Matriz de covariância aproximada:", covariancia)
