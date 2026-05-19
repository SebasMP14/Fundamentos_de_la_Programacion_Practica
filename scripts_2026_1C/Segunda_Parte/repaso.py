"""
Se pide un programa en Python que genere una matriz de M filas x N 
columnas, con numeros primos aleatorios entre 100 y 999
en las filas pares (incluido el 0), y no primos aleatorios en las 
filas impares.
Una vez generada la matriz se debe ordenar las filas de matriz de 
forma descendente utilizando InsertionSort.
Todas las operaciones deben realizarse mediante funciones.

1. Crear una funcion que devuelva si un numero es o no primo.
2. Crear una funcion donde se pida al usuario que ingrese el numero 
de filas y columnas de una matriz.
  La funcion debe devolver una tupla. No es necesario validar, asuma 
  que el usuario ingresará un numero positivo mayor a 4
3. Crear una funcion que genere una matriz de M x N como se pide en 
el enunciado.
4. Copie la funcion InsertionSort y modifique para ordenar el vector 
en forma descendente.
5. Imprima la matriz generada y despues de ordenar, utilizando una función.

def InsertionSort(array):
    N = len(array)
    for i in range(1,N):
        elem = array[i]
        j=i-1
        while j>=0 and array[j]>elem:
            #El elemento en array[j] se desplaza un lugar a la derecha
            array[j+1] = array[j]
            j=j-1
        #Se coloca el "nuevo" elemento en su lugar
        array[j+1] = elem

Criterios de Corrección:
30% Utilizacion de funciones
10% Funcion que retorna una tupla
30% Generar matriz con numeros primos y no primos aleatorios
15% Ordenar las filas de la matriz usando InsertionSort
10% Impresion de matriz
05% Solucion adecuada del problema. Impresion de mensajes al usuario

Recuerden:
Los estudiantes que tengan soluciones similares llevarán 0 %.

La evaluación será realizada manualmente.

Se puede resolver el ejercicio en el VPL o en el VSCODE(recuerde 
guardar cada paso en el VPL).
"""



# import random


# # ==========================================================
# # 1) FUNCION: VERIFICAR SI ES PRIMO
# # ==========================================================

# def es_primo(n):

#   if n < 2:
#     return False

#   i = 2
#   while i * i <= n:
#     if n % i == 0:
#       return False
#     i += 1

#   return True


# # ==========================================================
# # 2) FUNCION: INGRESO DE DIMENSIONES
# # ==========================================================

# def obtener_dimensiones():

#   filas = int(input("Ingrese cantidad de filas: "))
#   columnas = int(input("Ingrese cantidad de columnas: "))

#   return (filas, columnas)   # tupla


# # ==========================================================
# # 3) FUNCIONES AUXILIARES DE GENERACION
# # ==========================================================

# def generar_primo():

#   while True:
#     num = random.randint(100, 999)
#     if es_primo(num):
#       return num


# def generar_no_primo():
#   while True:
#     num = random.randint(100, 999)
#     if not es_primo(num):
#       return num


# # ==========================================================
# # 4) FUNCION: GENERAR MATRIZ
# # ==========================================================

# def generar_matriz(filas, columnas):
#   matriz = []

#   for i in range(filas):
#     fila = []
#     for j in range(columnas):

#       if i % 2 == 0:
#         valor = generar_primo()
#       else:
#         valor = generar_no_primo()

#       fila.append(valor)

#     matriz.append(fila)

#   return matriz


# # ==========================================================
# # 5) INSERTIONSORT DESCENDENTE
# # ==========================================================

# def insertion_sort_desc(vector):

#   for i in range(1, len(vector)):

#     actual = vector[i]
#     j = i - 1

#     # CAMBIO CLAVE: < en lugar de >
#     while j >= 0 and vector[j] < actual:
#       vector[j + 1] = vector[j]
#       j -= 1

#     vector[j + 1] = actual

#   return vector


# # ==========================================================
# # 6) ORDENAR MATRIZ POR FILAS
# # ==========================================================

# def ordenar_matriz(matriz):
#   for fila in matriz:
#     insertion_sort_desc(fila)


# # ==========================================================
# # 7) FUNCION: IMPRIMIR MATRIZ
# # ==========================================================

# def imprimir_matriz(matriz, mensaje):
#   print("\n" + mensaje)

#   for fila in matriz:
#     print(fila)


# # ==========================================================
# # 8) PROGRAMA PRINCIPAL
# # ==========================================================

# def main():
#   print("=== GENERADOR DE MATRIZ CON PRIMOS / NO PRIMOS ===")

#   # obtener dimensiones
#   m, n = obtener_dimensiones()

#   # generar matriz
#   matriz = generar_matriz(m, n)

#   # imprimir original
#   imprimir_matriz(matriz, "Matriz generada:")

#   # ordenar
#   ordenar_matriz(matriz)

#   # imprimir ordenada
#   imprimir_matriz(matriz, "Matriz ordenada (descendente por filas):")


# # ejecutar
# main()



"""
Una empresa de monitoreo energético desea analizar el comportamiento de consumo
de distintos dispositivos en una planta industrial.

Se pide desarrollar un programa en Python que:

1) Solicite al usuario dos valores enteros:
  - M (filas)
  - N (columnas)
  (Se asume que M y N son mayores o iguales a 5)

-----------------------------------------------------

2) Genere una matriz de M x N de la siguiente forma:

- En las filas con índice PAR:
  generar números ALEATORIOS entre 100 y 999 cuya
  SUMA DE DÍGITOS sea un número PRIMO.

- En las filas con índice IMPAR:
  generar números ALEATORIOS entre 100 y 999 cuya
  SUMA DE DÍGITOS NO sea un número PRIMO.

-----------------------------------------------------

3) Una vez generada la matriz, se debe:

- Ordenar cada fila utilizando el algoritmo de InsertionSort
- Pero con la siguiente condición:
* Si la fila es PAR → ordenar en forma ASCENDENTE
* Si la fila es IMPAR → ordenar en forma DESCENDENTE

-----------------------------------------------------

4) Luego, se debe construir un vector que contenga:

- El MAYOR valor de cada fila PAR
- El MENOR valor de cada fila IMPAR

-----------------------------------------------------

5) Sobre ese vector resultante:

- Ordenarlo utilizando el algoritmo de QUICKSORT
- Buscar un valor ingresado por el usuario utilizando BÚSQUEDA BINARIA

-----------------------------------------------------

6) Mostrar:

- Matriz original
- Matriz ordenada
- Vector construido
- Vector ordenado
- Resultado de la búsqueda

-----------------------------------------------------

FUNCIONES OBLIGATORIAS:

1) Función que determine si un número es primo
2) Función que calcule la suma de dígitos
3) Función que genere un número válido según condición
4) Función que genere la matriz
5) Función de InsertionSort (adaptada asc/desc)
6) Función de Quicksort
7) Función de Búsqueda Binaria
8) Función para imprimir estructuras

-----------------------------------------------------

CRITERIOS DE EVALUACION:

- Uso correcto de funciones (30%)
- Generación correcta de matriz (25%)
- Ordenación con condiciones (15%)
- Construcción del vector (10%)
- Implementación de búsqueda (10%)
- Salida clara y estructurada (10%)

"""

# import random
# # ==========================================================
# # 1) FUNCIONES MATEMATICAS
# # ==========================================================

# def es_primo(n):
#   if n < 2:
#     return False

#   i = 2
#   while i * i <= n:
#     if n % i == 0:
#       return False
#     i += 1

#   return True


# def suma_digitos(n):
#   suma = 0
#   while n > 0:
#     suma += n % 10
#     n = n // 10

#   return suma


# # ==========================================================
# # 2) GENERACION DE NUMEROS VALIDOS
# # ==========================================================

# def generar_numero(condicion_primo_suma):
#   while True:
#     num = random.randint(100, 999)
#     s = suma_digitos(num)

#     if condicion_primo_suma:
#       if es_primo(s):
#         return num
#     else:
#       if not es_primo(s):
#         return num


# # ==========================================================
# # 3) GENERAR MATRIZ
# # ==========================================================

# def generar_matriz(m, n):
#   matriz = []
#   for i in range(m):
#     fila = []

#     for j in range(n):
#       if i % 2 == 0:
#         valor = generar_numero(True)
#       else:
#         valor = generar_numero(False)

#       fila.append(valor)

#     matriz.append(fila)

#   return matriz


# # ==========================================================
# # 4) INSERTIONSORT ADAPTABLE
# # ==========================================================

# def insertion_sort(fila, asc=True):
#   for i in range(1, len(fila)):
#     actual = fila[i]
#     j = i - 1

#     if asc:
#       while j >= 0 and fila[j] > actual:
#         fila[j + 1] = fila[j]
#         j -= 1
#     else:
#       while j >= 0 and fila[j] < actual:
#         fila[j + 1] = fila[j]
#         j -= 1

#     fila[j + 1] = actual


# # ==========================================================
# # 5) ORDENAR MATRIZ CON CONDICION
# # ==========================================================

# def ordenar_matriz(matriz):
#   # for fila in matriz:
#   for i in range(len(matriz)):
#     if i % 2 == 0:
#       insertion_sort(matriz[i], asc=True)
#     else:
#       insertion_sort(matriz[i], asc=False)


# # ==========================================================
# # 6) CONSTRUIR VECTOR
# # ==========================================================

# def construir_vector(matriz):
#   vector = []
#   for i in range(len(matriz)):
#     fila = matriz[i]

#     if i % 2 == 0:
#       vector.append(max(fila))
#     else:
#       vector.append(min(fila))

#   return vector


# # ==========================================================
# # 7) QUICKSORT
# # ==========================================================

# def quicksort(lista):
#   if len(lista) <= 1:
#     return lista

#   pivote = lista[len(lista)//2]

#   menores = []
#   iguales = []
#   mayores = []

#   for x in lista:
#     if x < pivote:
#       menores.append(x)
#     elif x > pivote:
#       mayores.append(x)
#     else:
#       iguales.append(x)

#   return quicksort(menores) + iguales + quicksort(mayores)


# # ==========================================================
# # 8) BUSQUEDA BINARIA
# # ==========================================================

# def busqueda_binaria(lista, objetivo):
#   izq = 0
#   der = len(lista) - 1

#   while izq <= der:
#     mid = (izq + der) // 2
#     if lista[mid] == objetivo:
#       return mid
#     elif lista[mid] < objetivo:
#       izq = mid + 1
#     else:
#       der = mid - 1

#   return -1


# # ==========================================================
# # 9) IMPRESION
# # ==========================================================

# def imprimir_matriz(matriz, titulo):
#   print("\n" + titulo)
#   for fila in matriz:
#     print(fila)


# def imprimir_vector(vector, titulo):
#     print("\n" + titulo)
#     print(vector)


# # ==========================================================
# # 10) PROGRAMA PRINCIPAL
# # ==========================================================

# def main():
#   print("=== ANALISIS DE MATRIZ ===")

#   m = int(input("Ingrese filas (>=5): "))
#   n = int(input("Ingrese columnas (>=5): "))

#   matriz = generar_matriz(m, n)

#   imprimir_matriz(matriz, "Matriz original:")

#   ordenar_matriz(matriz)

#   imprimir_matriz(matriz, "Matriz ordenada:")

#   vector = construir_vector(matriz)

#   imprimir_vector(vector, "Vector construido:")

#   vector_ordenado = quicksort(vector)

#   imprimir_vector(vector_ordenado, "Vector ordenado (quicksort):")

#   valor = int(input("\nIngrese valor a buscar: "))

#   pos = busqueda_binaria(vector_ordenado, valor)

#   if pos != -1:
#     print("Valor encontrado en posicion:", pos)
#   else:
#     print("Valor no encontrado")


# # ejecutar
# main()











"""
Para este ejercicio, se desea analizar una matriz de números enteros y 
encontrar aquellas posiciones que presentan una pendiente local alta. 
La pendiente local de una celda se define como la diferencia entre el 
valor de esa celda y el promedio de sus vecinos adyacentes (solo se 
consideran los vecinos directo superior, inferior, izquierdo y derecho). 
En el caso de las posiciones ubicadas en los bordes de la matriz (primera 
fila, primera columna, última fila, última columna), se deberán considerar 
solamente los vecinos existentes.

El objetivo es determinar las cinco posiciones con mayor pendiente local 
de la matriz, junto con su valor de pendiente. En caso de que existan menos 
de cinco valores únicos de pendiente, se deben mostrar todas las posiciones 
posibles ordenadas de mayor a menor según el valor de la pendiente.

Requisitos del programa:

1.     Solicitar al usuario dos números enteros positivos M y N, 
correspondientes a las dimensiones de la matriz. Validar que ambos 
sean mayores a 1.

2.     Generar una matriz de M filas por N columnas con valores 
generados aleatoriamente en el rango de [10, 100].

3.     Calcular la pendiente local para cada celda de la matriz.

4.     Mostrar en pantalla:

o   La matriz generada.

o   Las cinco posiciones (i, j) con mayor pendiente local y el 
valor de dicha pendiente, ordenadas de mayor a menor.

Ejemplo de salida esperada:

Matriz generada:

14   22  9  33

 17   8  44 10

 11  23 31   6

 


Top 5 pendientes locales:
(1, 2): 29.5
(0, 3): 23.5
(0, 1): 11.67
(2, 2): 6.67
(2, 1): 6.33


 

Criterios de evaluación:

Ítem

Puntaje

Validación de las dimensiones de la matriz

10%

Generación aleatoria de la matriz

10%

Cálculo correcto de los vecinos válidos para cada celda

15%

Cálculo de la pendiente local para cada posición

15%

Almacenamiento correcto de posiciones con sus pendientes

10%

Selección y orden correcto de las cinco mayores pendientes

20%

Impresión clara y estructurada de resultados(con formato)

10%

Uso adecuado de funciones (mínimo dos funciones definidas por el alumno)

10%

Penalización por errores de sintaxis

-5% c/u

Recuerden:
Los estudiantes que tengan soluciones similares llevarán 0 %.

La evaluación será realizada será realizada manualmente.

Se puede resolver el ejercicio en el VPL o en el VSCODE(recuerde guardar cada paso en el VPL).
"""
import random

# ==========================================================
# 1) VALIDACION DE DIMENSIONES
# ==========================================================

def pedir_dimensiones():
  while True:
    m = int(input("Ingrese M (>1): "))
    n = int(input("Ingrese N (>1): "))

    if m > 1 and n > 1:
      return m, n
    else:
      print("Error: ambos deben ser mayores a 1")


# ==========================================================
# 2) GENERAR MATRIZ
# ==========================================================

def generar_matriz(m, n):
  matriz = []

  for i in range(m):
    fila = []
    for j in range(n):
      fila.append(random.randint(10, 100))
    matriz.append(fila)

  return matriz


# ==========================================================
# 3) OBTENER VECINOS VALIDOS
# ==========================================================

def obtener_vecinos(matriz, i, j):
  vecinos = []

  filas = len(matriz)
  columnas = len(matriz[0])

  # arriba
  if i - 1 >= 0:
    vecinos.append(matriz[i-1][j])

  # abajo
  if i + 1 < filas:
    vecinos.append(matriz[i+1][j])

  # izquierda
  if j - 1 >= 0:
    vecinos.append(matriz[i][j-1])

  # derecha
  if j + 1 < columnas:
    vecinos.append(matriz[i][j+1])

  return vecinos


# ==========================================================
# 4) CALCULAR PENDIENTE LOCAL
# ==========================================================

def calcular_pendiente(matriz):
  resultados = []

  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      vecinos = obtener_vecinos(matriz, i, j)

      promedio = sum(vecinos) / len(vecinos)

      pendiente = matriz[i][j] - promedio

      resultados.append((pendiente, i, j))

  return resultados


# ==========================================================
# 5) ORDENAR (SELECCION DESCENDENTE)
# ==========================================================

def ordenar_desc(lista):
  for i in range(len(lista)):

    max_idx = i

    for j in range(i+1, len(lista)):
      if lista[j][0] > lista[max_idx][0]:
        max_idx = j

    lista[i], lista[max_idx] = lista[max_idx], lista[i]


# ==========================================================
# 6) IMPRIMIR MATRIZ
# ==========================================================

def imprimir_matriz(matriz):
  print("\nMatriz generada:\n")

  for fila in matriz:
    for val in fila:
      print(f"{val:4}", end=" ")
    print()


# ==========================================================
# 7) MOSTRAR TOP 5
# ==========================================================

def mostrar_top(resultados):
  print("\nTop pendientes locales:")

  limite = 5 if len(resultados) >= 5 else len(resultados)

  for k in range(limite):
    pendiente, i, j = resultados[k]
    print(f"({i}, {j}): {round(pendiente, 2)}")


# ==========================================================
# 8) PROGRAMA PRINCIPAL
# ==========================================================

def main():
  m, n = pedir_dimensiones()

  matriz = generar_matriz(m, n)

  imprimir_matriz(matriz)

  resultados = calcular_pendiente(matriz)

  ordenar_desc(resultados)

  mostrar_top(resultados)


# ejecutar
main()