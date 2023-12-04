import numpy as np
import matplotlib.pyplot as plt

# Tamaño de la malla
size = 100

# Crear una malla de puntos para simular el campo electromagnético
grid = np.zeros((size, size))

# Punto fuente de la onda
source_x, source_y = size // 2, size // 2
grid[source_x, source_y] = 1

# Solicitar al usuario el valor del coeficiente
coefficient = float(input("Ingrese el valor del coeficiente para la actualización de la onda (recomendado 0.5 - 1.0): "))

# Simulación de la propagación de la onda
for t in range(100):
    new_grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            new_grid[i, j] = grid[i, j] + coefficient * (
                grid[(i + 1) % size, j] +
                grid[(i - 1) % size, j] +
                grid[i, (j + 1) % size] +
                grid[i, (j - 1) % size] -
                4 * grid[i, j]
            )
    grid = new_grid

    # Visualización de la simulación para cada 10 iteraciones
    if t % 10 == 0:
        plt.imshow(grid, cmap='viridis')
        plt.title(f'Tiempo: {t}')
        plt.colorbar()
        plt.show()
