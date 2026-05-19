# """
# UNIDAD: INTRODUCCIÓN A NUMPY - ARREGLOS MULTIDIMENSIONALES

# OBJETIVO:
# - Comprender el uso de numpy para cálculo numérico eficiente
# - Trabajar con arreglos multidimensionales (vectores, matrices, tensores)
# - Utilizar funciones clave de numpy en problemas de ingeniería
# - Resolver ejercicios aplicando múltiples herramientas de numpy

# IMPORTANTE:
# Instalar numpy si no está disponible:
# pip install numpy
# """

# # ==========================================================
# # 1) IMPORTACION
# # ==========================================================

import numpy as np


# # ==========================================================
# # 2) CREACION DE ARREGLOS
# # ==========================================================

"""
Funciones clave:
- np.array
- np.zeros
- np.ones
- np.eye
- np.arange
- np.linspace
- np.random
"""

a = np.array([1, 2, 3])
b = np.zeros((2, 3))
c = np.ones((3, 3))
d = np.eye(3)
e = np.arange(0, 10, 2.5)
f = np.linspace(0, 1, 5)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)


# # ==========================================================
# # 3) ARREGLOS MULTIDIMENSIONALES
# # ==========================================================

mat = np.array([ [1, 2, 3],
                 [4, 5, 6] ])

tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

# print(mat.shape())
print(tensor.shape)
print(np.sum(tensor))


# # ==========================================================
# # 4) OPERACIONES VECTORIALES
# # ==========================================================

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)
print(x * y)
print(x ** 2)
z = np.sqrt(x)
print(z)
print(np.sqrt(x))
print(np.exp(x))
print(np.log(x))
# np.


# # ==========================================================
# # 5) AGREGACIONES
# # ==========================================================

data = np.array([[1, 2, 3],
                [4, 5, 6]])

matriz = [ [1, 2, 3], [3, 4, 5], [5, 6, 7]]
print("MATRIZ: ", matriz)
d = np.array(matriz)
print("DDDD: ", d)

print(np.sum(data))
print(np.sum(data, axis=0))  # columnas
print(np.sum(data, axis=1))  # filas
print(np.mean(data))
print(np.max(data))
print(np.min(data))


# # ==========================================================
# # 6) MANIPULACION
# # ==========================================================

arr = np.arange(6)

mat = arr.reshape((2, 3))
# print(mat)

# print(mat.T)
# print(mat.flatten())


# # ==========================================================
# # 7) FUNCIONES IMPORTANTES
# # ==========================================================

# """
# np.sort
# np.argsort
# np.unique
# np.where
# np.clip
# np.round
# """

arr = np.array([5, 2, 8, 2, 1])

# print(np.sort(arr))
# print(np.argsort(arr))
# print(np.unique(arr))
# print(np.where(arr > 3))
# print(np.clip(arr, 2, 6))


# # ==========================================================
# # 8) ALGEBRA LINEAL
# # ==========================================================

A = np.array([[1, 2], [3, 4]])

# print(np.linalg.det(A))
# print(np.linalg.inv(A))
# print(np.dot(A, A))


# # ==========================================================
# # 9) EJERCICIO 1 – ANALISIS DE MATRIZ
# # ==========================================================

"""
Generar una matriz NxM aleatoria entre 1 y 100.
Calcular:
- suma por filas y columnas
- promedio total
- valores mayores al promedio
"""

N = 4
M = 5

mat = np.random.randint(0, 101, (N, M))
# print("Matriz:\n", mat)
suma_filas = np.sum(mat, axis=1)
suma_columnas = np.sum(mat, axis=0)
promedio = np.mean(mat)

mayores = mat[mat > promedio]

print("Suma filas:", suma_filas)
print("Suma columnas:", suma_columnas)
print("Promedio:", promedio)
print("Mayores al promedio:", mayores)


# # ==========================================================
# # 10) EJERCICIO 2 – NORMALIZACION Y FILTRADO
# # ==========================================================

"""
Dada una matriz:
- normalizar valores entre 0 y 1
- reemplazar valores < 0.5 por 0
- contar cuantos valores quedaron
"""

mat = np.random.randint(1, 100, (3, 3))

max_val = np.max(mat)
norm = mat / max_val

filtrado = np.where(norm < 0.5, 0, norm)

cantidad = np.count_nonzero(filtrado)

# print("Original:\n", mat)
# print("Normalizada:\n", norm)
# print("Filtrada:\n", filtrado)
# print("Cantidad no cero:", cantidad)


# # ==========================================================
# # 11) EJERCICIO 3 – ANALISIS DE FILAS
# # ==========================================================

"""
Dada una matriz NxN:
- encontrar la fila con mayor suma
- ordenar esa fila
"""

mat = np.random.randint(1, 50, (4, 4))

suma_filas = np.sum(mat, axis=1)
idx = np.argmax(suma_filas)

fila = mat[idx]
fila_ordenada = np.sort(fila)

# print("Matriz:\n", mat)
# print("Fila con mayor suma:", fila)
# print("Ordenada:", fila_ordenada)


# # ==========================================================
# # 12) EJERCICIO 4 – PRODUCTO Y PROPIEDADES
# # ==========================================================

"""
Dadas dos matrices:
- verificar si se pueden multiplicar
- calcular producto
- calcular determinante si es cuadrada
"""

# A = np.random.randint(1, 10, (2, 3))
# B = np.random.randint(1, 10, (3, 2))

# if A.shape[1] == B.shape[0]:
#     C = np.dot(A, B)
#     print("Producto:\n", C)

#     if C.shape[0] == C.shape[1]:
#         print("Determinante:", np.linalg.det(C))


# # ==========================================================
# # 13) EJERCICIO 5 – DETECCION DE PATRONES
# # ==========================================================

# """
# Dada una matriz:
# - encontrar valores únicos
# - contar frecuencia de cada valor
# """

# mat = np.random.randint(1, 6, (4, 4))

# valores, conteo = np.unique(mat, return_counts=True)

# print("Matriz:\n", mat)
# print("Valores:", valores)
# print("Frecuencia:", conteo)


# # ==========================================================
# # 14) CONCLUSION
# # ==========================================================

# """
# NUMPY permite:
# - simplificar código
# - mejorar rendimiento
# - trabajar con datos reales

# IDEA CLAVE:
# Resolver problemas usando operaciones vectorizadas
# en lugar de ciclos tradicionales.
# """