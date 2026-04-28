# # BUSQUEDA LINEAL

# """
# IDEA:
# Recorrer todos los elementos uno por uno.

# VENTAJA:
# - Simple
# - Funciona siempre

# DESVENTAJA:
# - Lento para grandes cantidades
# """

# def busqueda_lineal(lista, objetivo):
#   for i in range(len(lista)):
#     if lista[i] == objetivo:
#       return i  # posición donde se encontró

#   return -1  # no encontrado


# # ejemplo
# datos = [10, 5, 8, 20, 3]

# pos = busqueda_lineal(datos, 8)

# print("Posicion:", pos)



# BUSQUEDA BINARIA

"""
REQUISITO:
La lista debe estar ORDENADA.

IDEA:
Dividir el problema en mitades.

1) comparar con el medio
2) descartar la mitad incorrecta
3) repetir

VENTAJA:
- Muy rápida

DESVENTAJA:
- Requiere lista ordenada
"""

def busqueda_binaria(lista, objetivo):
  izquierda = 0
  derecha = len(lista) - 1

  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2

    if lista[medio] == objetivo:
      return medio
    elif lista[medio] < objetivo:
      izquierda = medio + 1
    else:
      derecha = medio - 1

  return -1


# # ejemplo
# datos = [3, 5, 8, 10, 20]

# pos = busqueda_binaria(datos, 10)

# print("Posicion:", pos)




# TIEMPO DE EJECUCION

"""
No medimos en segundos, sino en cantidad de operaciones.

Búsqueda lineal:
- peor caso: revisar todos los elementos
- O(n)

Búsqueda binaria:
- divide el problema a la mitad cada vez
- O(log n)

Ejemplo:
n = 1000

lineal → hasta 1000 comparaciones
binaria → ~10 comparaciones

----------------------------------------

# IDEA CLAVE:

# Si podes ordenar → usa binaria
# Si no → usa lineal
# """




# ORDENACION POR SELECCION

"""
IDEA:
1) buscar el menor elemento
2) colocarlo al inicio
3) repetir con el resto

VENTAJA:
- Fácil de entender

DESVENTAJA:
- Siempre O(n²)
"""

# def seleccion(lista):
#   n = len(lista)

#   for i in range(n):
#     min_idx = i

#     for j in range(i+1, n):
#       if lista[j] < lista[min_idx]:
#         min_idx = j

#     # intercambiar
#     lista[i], lista[min_idx] = lista[min_idx], lista[i]

#   return lista


# # ejemplo
# datos = [10, 5, 8, 20, 3]

# print(seleccion(datos))





# ORDENACION POR INSERCION

"""
IDEA:
Construir la lista ordenada insertando elementos.

VENTAJA:
- Bueno para listas pequeñas o casi ordenadas

DESVENTAJA:
- O(n²) en peor caso
"""

def insercion(lista):

  for i in range(1, len(lista)):
    actual = lista[i]
    j = i - 1

    while j >= 0 and lista[j] > actual:
      lista[j+1] = lista[j]
      j -= 1

    lista[j+1] = actual

  return lista


# # ejemplo
# datos = [10, 5, 8, 20, 3]

# print(insercion(datos))



# # COMPARACION DE ALGORITMOS

# """
# BUSQUEDA:

# Lineal:
# - no requiere orden
# - O(n)

# Binaria:
# - requiere orden
# - O(log n)

# ----------------------------------------

# ORDENACION:

# Selección:
# - siempre O(n²)

# Inserción:
# - O(n²) peor caso
# - mejor si lista casi ordenada

# ----------------------------------------

# IDEA DE INGENIERÍA:

# Elegir algoritmo según:
# - tamaño de datos
# - estado de los datos
# - restricciones del problema
# """




# # VERSION CON CONTEO DE OPERACIONES

def busqueda_lineal_cont(lista, objetivo):

  comparaciones = 0

  for i in range(len(lista)):
    comparaciones += 1

    if lista[i] == objetivo:
      return i, comparaciones

  return -1, comparaciones


def busqueda_binaria_cont(lista, objetivo):

  izquierda = 0
  derecha = len(lista) - 1
  comparaciones = 0

  while izquierda <= derecha:

    medio = (izquierda + derecha) // 2
    comparaciones += 1

    if lista[medio] == objetivo:
      return medio, comparaciones

    elif lista[medio] < objetivo:
      izquierda = medio + 1
    else:
      derecha = medio - 1

  return -1, comparaciones


# programa principal

n = int(input("Cantidad de datos: "))

datos = []

for i in range(n):
  datos.append(int(input("Numero: ")))

x = int(input("Valor a buscar: "))

ordenados = insercion(datos.copy())

print("Lista ordenada:", ordenados)

pos1, c1 = busqueda_lineal_cont(datos, x)
pos2, c2 = busqueda_binaria_cont(ordenados, x)

print("Lineal -> Pos:", pos1, "Comparaciones:", c1)
print("Binaria -> Pos:", pos2, "Comparaciones:", c2)


















# #########################################################################################################################################
# """
# ENUNCIADO:

# Se desea analizar una secuencia de números generados
# a partir de una expresión matemática.

# 1) El usuario debe ingresar:
#    - Un número entero positivo N (N >= 5)
#    - Un número entero positivo K

# 2) Generar una lista de N números enteros positivos
#    utilizando la siguiente fórmula:

#         f(i) = i^3 - 4*i + 7

#    para i desde 1 hasta N

# -----------------------------------------------------

# 3) FILTRADO:

# De la lista generada, se deben considerar SOLO aquellos números que:

# - Tengan una cantidad PAR de divisores
# - Y cuya suma de divisores propios sea MAYOR que el propio número

# (Los números que cumplen esta condición se llaman "ABUNDANTES")

# -----------------------------------------------------

# 4) ORDENACIÓN:

# Ordenar los números filtrados utilizando
# EXCLUSIVAMENTE el algoritmo de ORDENACIÓN POR SELECCIÓN.

# Ordenar en forma ASCENDENTE.

# -----------------------------------------------------

# 5) BÚSQUEDA:

# Buscar el K-ésimo número cuya suma de dígitos es primo
# utilizando BÚSQUEDA BINARIA.

# IMPORTANTE:
# - Si existen menos de K números cuya suma sean primos → indicar error

# -----------------------------------------------------

# 6) SALIDA:

# Mostrar:

# - Lista generada original
# - Lista filtrada (antes de ordenar)
# - Lista ordenada
# - El número cuya suma de digitos sea primo encontrado (si existe)
# - Su posición en la lista ordenada

# -----------------------------------------------------

# RESTRICCIONES:

# - NO usar funciones de ordenación de Python
# - NO usar librerías externas
# - Implementar:
#   * función de generación
#   * función de divisores
#   * ordenación por selección
#   * búsqueda binaria
#   * verificación de número

# ------------------------------------------------------------
# Entrada:
# N = 10
# K = 1

# Salida:
# Lista original: [...]
# Lista filtrada: [...]
# Lista ordenada: [...]
# Número perfecto encontrado: 6
# Posición: 2
# ------------------------------------------------------------
# """


# ==========================================================
# GENERAR LISTA
# ==========================================================

# def generar_lista(N):
#   lista = []

#   for i in range(1, N+1):
#     valor = i**3 - 4*i + 7
#     lista.append(valor)

#   return lista


# # ==========================================================
# # SUMA DE DIVISORES PROPIOS
# # ==========================================================

# def suma_divisores(n):
#   suma = 0

#   for i in range(1, n):
#     if n % i == 0:
#       suma += i

#   return suma


# # ==========================================================
# # CANTIDAD DE DIVISORES
# # ==========================================================

# def cantidad_divisores(n):
#   contador = 0

#   for i in range(1, n+1):
#     if n % i == 0:
#       contador += 1

#   return contador


# # ==========================================================
# # NUMERO ABUNDANTE
# # ==========================================================

# def es_abundante(n):
#   return suma_divisores(n) > n


# # ==========================================================
# # SUMA DE DIGITOS
# # ==========================================================

# def suma_digitos(n):
#   suma = 0

#   while n > 0:
#     suma += n % 10
#     n = n // 10

#   return suma

# # ==========================================================
# # NUMERO PRIMO
# # ==========================================================

# def es_primo(n):
#   if n < 2:
#     return False

#   for i in range(2, n):
#     if n % i == 0:
#       return False

#   return True


# # ==========================================================
# # FILTRAR LISTA
# # ==========================================================

# def filtrar(lista):
#   filtrados = []

#   for num in lista:
#     if cantidad_divisores(num) % 2 == 0 and es_abundante(num):
#       filtrados.append(num)

#   return filtrados


# # ==========================================================
# # ORDENACION POR SELECCION
# # ==========================================================

# def seleccion(lista):
#   n = len(lista)

#   for i in range(n):

#     min_idx = i

#     for j in range(i+1, n):
#       if lista[j] < lista[min_idx]:
#         min_idx = j

#     lista[i], lista[min_idx] = lista[min_idx], lista[i]

#   return lista


# # ==========================================================
# # OBTENER K-ESIMO PERFECTO
# # ==========================================================

# def obtener_k_esimo_perfecto(lista, K):
#   contador = 0

#   for num in lista:
#     if es_primo(suma_digitos(num)):
#       contador += 1

#       if contador == K:
#         return num

#   return None


# # ==========================================================
# # BUSQUEDA BINARIA
# # ==========================================================

# def busqueda_binaria(lista, objetivo):
#   izquierda = 0
#   derecha = len(lista) - 1

#   while izquierda <= derecha:
#     medio = (izquierda + derecha) // 2

#     if lista[medio] == objetivo:
#       return medio
#     elif lista[medio] < objetivo:
#       izquierda = medio + 1
#     else:
#       derecha = medio - 1

#   return -1


# # ==========================================================
# # PROGRAMA PRINCIPAL
# # ==========================================================

# # VALIDACION
# N = 0
# while N < 5:
#   N = int(input("Ingrese N (>=5): "))

# K = 0
# while K <= 0:
#   K = int(input("Ingrese K (>0): "))


# # 1) GENERAR
# original = generar_lista(N)
# print("Lista original:", original)


# # 2) FILTRAR
# filtrados = filtrar(original)
# print("Lista filtrada:", filtrados)


# # 3) ORDENAR
# ordenados = seleccion(filtrados.copy())
# print("Lista ordenada:", ordenados)


# # 4) OBTENER K-ESIMO PERFECTO
# objetivo = obtener_k_esimo_perfecto(ordenados, K)

# if objetivo is None:
#   print("No existen", K, "suma de dígitos que sean primos")
# else:
#   print("Numero k-esimo cuya suma de dígitos es primo encontrado:", objetivo)

#   # 5) BUSQUEDA BINARIA
#   pos = busqueda_binaria(ordenados, objetivo)

#   print("Posicion en lista ordenada:", pos)