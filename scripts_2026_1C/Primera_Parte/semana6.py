
# """ENUNCIADO

# Un número triangular T(n) es la suma de todos los números
# naturales desde 1 hasta n.

# Ejemplos
# T(2) = 1 + 2 = 3
# T(5) = 1 + 2 + 3 + 4 + 5 = 15

# Un número es BUENO si la suma de sus cifras es un número triangular.
# En caso contrario es MALO.

# El programa debe determinar si cada número es BUENO o MALO.

# Entrada
# Primera línea: N
# Luego N números enteros positivos.

# Salida
# N líneas con:
# BUENO
# o
# MALO
# """

# N = int(input())

# for i in range(N):

#     numero = input()

#     # calcular suma de cifras
#     suma = 0

#     for d in numero:
#         suma = suma + int(d)

#     # verificar si suma es triangular
#     triangular = False

#     acumulado = 0
#     n = 1

#     while acumulado < suma:

#         acumulado = acumulado + n

#         if acumulado == suma:
#             triangular = True

#         n = n + 1

#     if triangular:
#         print("BUENO")
#     else:
#         print("MALO")



# """
# ENUNCIADO

# El programa recibe N números enteros y debe determinar
# cuántos de ellos son pares.

# Entrada
# Primera línea: N
# Luego N números.

# Salida
# Cantidad de números pares.
# """
# N = int(input("Cantidad de numeros: "))
# numeros = []
# for i in range(N):
#     n = int(input())
#     numeros.append(n)

# pares = 0
# PARES = []

# for n in numeros:
#     if n % 2 == 0:
#         PARES.append(n)
#         pares = pares + 1
#         # pares += 1

# print("Cantidad de pares:", pares)
# for i in range(pares):
#     print("Nro par ", i+1, ": ", PARES[i])









# """
# ENUNCIADO

# Dada una lista de N números, determinar cuál de ellos
# tiene la mayor suma de cifras.

# Entrada
# N
# N números

# Salida
# Número con mayor suma de cifras.
# """



# N = int(input())

# numeros = []

# for i in range(N):
#     numeros.append(input())

# mayor_suma = -1
# numero_resultado = ""

# for numero in numeros:

#     suma = 0

#     for d in numero:
#         suma = suma + int(d)

#     if suma > mayor_suma:
#         mayor_suma = suma
#         numero_resultado = numero

# print("Numero con mayor suma de cifras:", numero_resultado)







# """
# ENUNCIADO

# Un número es CRECIENTE si cada cifra es mayor
# o igual que la anterior.

# Ejemplos
# 1234 -> CRECIENTE
# 1129 -> CRECIENTE
# 321 -> NO CRECIENTE

# Determinar para cada número si es CRECIENTE.
# """



N = int(input())

for i in range(N):

    numero = input()

    creciente = True

    for j in range(len(numero) - 1):

        if numero[j] > numero[j+1]:
            creciente = False

    if creciente:
        print("CRECIENTE")
    else:
        print("NO CRECIENTE")








"""
ENUNCIADO

Un número es palíndromo si se lee igual de izquierda a derecha
que de derecha a izquierda.

Determinar si cada número de una lista es palíndromo.

Entrada
N
N números

Salida
Para cada número imprimir:
PALINDROMO
NO PALINDROMO
"""