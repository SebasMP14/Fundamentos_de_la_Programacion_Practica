import matplotlib.pyplot as plt
import numpy as np

# Datos con listas de Python
x_lista = [1, 2, 3, 4, 5]
y_lista = [i**2 for i in x_lista]

# Datos con arrays de NumPy
x_array = np.array([1, 2, 3, 4, 5])
y_array = x_array ** 3

# Crear la figura
plt.figure(figsize=(8, 5))

# Gráfico usando listas
plt.plot(x_lista, y_lista, 'o--', label='Listas de Python')

# Gráfico usando arrays de NumPy
plt.plot(x_array, y_array, 's-', label='Arrays de NumPy')

# Personalizar
plt.title("Comparación: Listas vs Arrays")
plt.xlabel("x")
plt.ylabel("x²")
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()



"""
Otra libreria
"""
import plotly.graph_objects as go
import plotly.io as pio