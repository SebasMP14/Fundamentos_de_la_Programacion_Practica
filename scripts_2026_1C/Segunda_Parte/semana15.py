# # ==========================================================
# # 1) ESCRITURA DE ARCHIVOS DE TEXTO
# # ==========================================================

# """
# MODOS:
# "w" → escritura (sobrescribe)
# "a" → agregar (append)
# """

# escribir datos en archivo
# archivo = open("datos.txt", "a")

# archivo.write("10\n")
# archivo.write("20\n")
# archivo.write("30\n")

# archivo.close()


# forma recomendada (automática)
with open("datos.txt", "a") as archivo:
    archivo.write("5\n")
    archivo.write("15\n")
    archivo.write("25\n")


# # ==========================================================
# # 2) LECTURA DE ARCHIVOS
# # ==========================================================

"""
Leer línea por línea
"""

datos = []

with open("datos.txt", "r") as archivo:

    for linea in archivo:
        numero = int(linea.strip())
        datos.append(numero)

# print("Datos leídos:", datos)



# # ==========================================================
# # 3) PROCESAMIENTO DE DATOS
# # ==========================================================

"""
Ejemplo:
- calcular promedio
- encontrar máximo y mínimo
"""

import numpy as np

arr = np.array(datos)

# print("Promedio:", np.mean(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))



# # ==========================================================
# # 4) INTRODUCCION A MATPLOTLIB
# # ==========================================================

import matplotlib.pyplot as plt

"""
Matplotlib permite:
- gráficos de líneas
- histogramas
- visualización de datos

Idea clave:
Convertir números en gráficos interpretables
"""




# # ==========================================================
# # 5) GRAFICO SIMPLE
# # ==========================================================

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 15, 25]

# plt.plot(x, datos)
# plt.title("Grafico simple")
# plt.xlabel("X")
# plt.ylabel("datos")
# plt.show()




# # ==========================================================
# # 6) HISTOGRAMAS
# # ==========================================================

# """
# Un histograma muestra:
# - distribución de los datos
# - frecuencia de valores
# """

# datos = np.random.randint(0, 100, 50)

# print("datos: ", datos)
# plt.hist(datos, bins=10)
# plt.title("Histograma")
# plt.xlabel("Valores")
# plt.ylabel("Frecuencia")
# plt.show()






# # ==========================================================
# # 7) EJEMPLO COMPLETO (ARCHIVO + HISTOGRAMA)
# # ==========================================================

"""
1) Leer datos desde archivo
2) Convertir a arreglo
3) Mostrar histograma
"""

datos = []

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        datos.append(int(linea.strip()))

arr = np.array(datos)

plt.hist(arr, orientation='horizontal')
plt.title("Distribucion de datos")
plt.show()






# # ==========================================================
# # 8) EJERCICIO PROPUESTO 1
# # ==========================================================

# """
# Leer un archivo con N números enteros.

# Calcular:
# - promedio
# - cantidad de números mayores al promedio

# Mostrar:
# - resultados
# - histograma de los datos
# """





# # ==========================================================
# # 9) EJERCICIO PROPUESTO 2
# # ==========================================================

# """
# Generar 100 números aleatorios entre 1 y 100
# y guardarlos en un archivo.

# Luego:
# - leer el archivo
# - separar números pares e impares
# - graficar dos histogramas:
#     uno para pares
#     otro para impares
# """





# # ==========================================================
# # 12) EJERCICIO PROPUESTO 3 (NIVEL EXAMEN)
# # ==========================================================

# """
# Un archivo contiene temperaturas registradas.

# El programa debe:

# 1) Leer los datos
# 2) Normalizar (dividir entre el máximo)
# 3) Filtrar valores > 0.7
# 4) Mostrar:
#     - cantidad de valores filtrados
#     - promedio de los filtrados
# 5) Graficar histograma de los valores originales y filtrados
# """




# # ==========================================================
# # 13) CONCLUSION
# # ==========================================================

# """
# - Los Archivos permiten trabajar con datos reales
# - NumPy facilita el procesamiento
# - Matplotlib permite interpretar visualmente

# FLUJO DE TRABAJO:

# Archivo → Lectura → Procesamiento → Visualización

# """