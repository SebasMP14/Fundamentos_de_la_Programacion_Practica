
"""
    NumPy es una librería de Python para cálculo numérico 
    rápido y eficiente.
Ideal para trabajar con vectores, matrices y operaciones 
matemáticas avanzadas.

Ventajas:
- Velocidad y rendimiento (usa código C por debajo).
- Facilita el trabajo con datos científicos.
- Muchas librerías como Pandas, SciPy o Scikit-learn 
dependen de NumPy."""
import numpy as np
# instalacion numpy: pip install numpy
a = np.array([1, 2, 3])             # Arreglo 1D
b = np.array([[1, 2], [3, 4]])      # Arreglo 2D (matriz)

np.zeros((2, 3))       # Matriz 2x3 llena de ceros
np.ones((3, 3))        # Matriz 3x3 llena de unos
np.eye(3)              # Matriz identidad 3x3
print(np.arange(0, 10, 2))    # [0, 2, 4, 6, 8]
print(np.linspace(0, 120, 5))   # 5 valores entre 0 y 1

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)     # (2, 3)
# d = a.ndim      # 2 dimensiones
# e = a.size      # 6 elementos
# print(c, d, e)

print("matriz a:", a)
print(a[0, 1])     # Fila 0, columna 1 → 2
print(a[1])        # Segunda fila: [4, 5, 6]
print(a[:, 1])     # Segunda columna: [2, 5]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b       # [5 7 9]
a * 2       # [2 4 6]
a @ b       # Producto punto: 1*4 + 2*5 + 3*6 = 32

arr3d = np.array([
  [[1, 2], [3, 4]],
  [[5, 6], [7, 8]]
])


"""
Crear un array 2D de tamaño 4x3 con np.arange.

Extraer la última columna.

Calcular la suma por filas y por columnas.
"""


arr = np.arange(12).reshape(4, 3)
print(arr)

ultima_columna = arr[:, 2]
print(ultima_columna)

suma_filas = arr.sum(axis=1)
suma_columnas = arr.sum(axis=0)

print("Suma por filas:", suma_filas)
print("Suma por columnas:", suma_columnas)



"""
Sensor de temperatura
Supongamos que un sensor registró la temperatura cada hora durante 3 días (72 datos).

Crear un array 3x24 (3 días, 24 horas).

Calcular la temperatura media de cada día.

Extraer el día con mayor temperatura media.
"""
# Simulación de datos
datos = np.random.normal(loc=25, scale=3, size=(3, 24))

# Media diaria
media_diaria = datos.mean(axis=1)

# Día con mayor temperatura media
dia_mas_calido = np.argmax(media_diaria)
