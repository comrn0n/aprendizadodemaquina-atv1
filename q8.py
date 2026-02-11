import numpy as np

img = np.array([[10, 255, 10], [50, 200, 50]])
mask = np.array([[0, 1, 0], [1, 0, 1]])

result = img * mask
print("O resultado da aplicação da máscara na imagem é:\n", result)