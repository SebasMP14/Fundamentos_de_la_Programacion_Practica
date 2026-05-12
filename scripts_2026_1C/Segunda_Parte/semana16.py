# ==========================================================
# QUICKSORT – IDEA FUNDAMENTAL
# ==========================================================

"""
IDEA PRINCIPAL:
"Dividir alrededor de un pivote"

PASOS:

1) Elegir un elemento de la lista → PIVOTE
2) Reordenar la lista de forma que:
   - menores al pivote → izquierda
   - mayores al pivote → derecha
3) Aplicar el mismo proceso recursivamente a cada lado

----------------------------------------

EJEMPLO:
def funcion([...]):
lista = [8, 3, 1, 7, 0, 10, 2]

Elegimos pivote = 7
Menores: [3, 1, 0, 2]
Mayores: [8, 10]

Resultado parcial:
return funcion([3, 1, 0, 2]) + [7] + funcion([8, 10])

Luego se repite el proceso en cada lado.

----------------------------------------

INTUICION:
Divide el problema en partes más pequeñas,
pero SIN crear copias completas (en versión óptima).

----------------------------------------

TIEMPO DE EJECUCION:
Mejor caso: O(n log n)
Caso promedio: O(n log n)
Peor caso: O(n²) ← si el pivote es malo (lista ya ordenada)

----------------------------------------

VENTAJA:
Muy rápido en la práctica

DESVENTAJA:
Peor caso puede ser malo
"""


# ==========================================================
# MERGESORT – IDEA FUNDAMENTAL
# ==========================================================


"""
IDEA PRINCIPAL:
"Dividir en mitades y luego mezclar ordenadamente"

PASOS:

1) Dividir la lista en dos mitades
2) Ordenar cada mitad recursivamente
3) Combinar (merge) ambas mitades ordenadas

----------------------------------------

EJEMPLO:

lista = [8, 3, 1, 7]

Dividir:
[8, 3]   [1, 7]

Dividir otra vez:
[8] [3]   [1] [7]

Ahora combinar ordenando:
[3, 8]   [1, 7]

Combinar final:
[1, 3, 7, 8]

----------------------------------------

Divide hasta lo más pequeño posible,
luego reconstruye ordenadamente.

----------------------------------------

TIEMPO DE EJECUCION:
Siempre: O(n log n)

----------------------------------------

VENTAJA:
Siempre eficiente (estable)

DESVENTAJA:
Usa memoria extra (crea listas nuevas)
"""


# ==========================================================
# 1) QUICKSORT – IMPLEMENTACION
# ==========================================================

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    menores = []
    iguales = []
    mayores = []

    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)

    return quicksort(menores) + iguales + quicksort(mayores)


# ejemplo
datos = [8, 3, 1, 7, 0, 10, 2]
print("Quicksort:", quicksort(datos))

# ==========================================================
# 2) MERGESORT – IMPLEMENTACION
# ==========================================================

def merge(izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # agregar lo restante
    resultado += izq[i:]
    resultado += der[j:]

    return resultado


def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return merge(izquierda, derecha)


# ejemplo
datos = [8, 3, 1, 7, 0, 10, 2]
print("Mergesort:", mergesort(datos))

# ==========================================================
# 3) COMPARACION DE TIEMPO (INTUITIVO)
# ==========================================================

"""
Simulación simple contando operaciones
"""

def quicksort_count(lista):
    if len(lista) <= 1:
        return lista, 0

    pivote = lista[len(lista) // 2]
    menores, iguales, mayores = [], [], []
    operaciones = 0

    for x in lista:
        operaciones += 1
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)

    izq, op1 = quicksort_count(menores)
    der, op2 = quicksort_count(mayores)

    return izq + iguales + der, operaciones + op1 + op2

# import random

# N = 10000000000
# datos = [random.randint(1, 10000) for _ in range(N)]
# print("Lista desordenada: ", datos)
# ordenada, count = quicksort_count(datos)

# print("Lista ordenada: ", ordenada)
# print("Conteo de operaciones: ", count)
# ==========================================================
# 4) EJERCICIO GUIADO
# ==========================================================

"""
ENUNCIADO:

1) Generar una lista de N números aleatorios
2) Ordenarla con:
   - quicksort
   - mergesort
3) Verificar que ambas listas son iguales
4) Contar operaciones aproximadas
"""

import random

N = 10
datos = [random.randint(1, 100) for _ in range(N)]

print("Original:", datos)

q = quicksort(datos)
m = mergesort(datos)

print("Quick:", q)
print("Merge:", m)

print("Son iguales:", q == m)





"""

ENUNCIADO:
Una empresa registra mediciones de vibración de una máquina
industrial durante N intervalos de tiempo.

Se pide desarrollar un programa que:
1) Ingrese un número entero N (N >= 10)
2) Genere una lista de N valores enteros positivos utilizando la función:
        f(i) = (i^2 + 3*i + 7) % 1000 + 50
para i desde 1 hasta N

-----------------------------------------------------

3) ORDENACION GLOBAL:
Ordenar TODA la lista utilizando MERGESORT.

-----------------------------------------------------

4) SEGMENTACION:
Dividir la lista ordenada en dos partes:
- Primera mitad: valores <= mediana
- Segunda mitad: valores > mediana

(La mediana se define como el elemento central de la lista ordenada)

-----------------------------------------------------

5) ORDENACION LOCAL:
- Ordenar la PRIMERA mitad en forma DESCENDENTE usando QUICKSORT
- Ordenar la SEGUNDA mitad en forma ASCENDENTE usando QUICKSORT

IMPORTANTE:
→ No usar reverse()

-----------------------------------------------------

6) RECONSTRUCCION:
Unir ambas mitades en una sola lista:
[primera_mitad_descendente + segunda_mitad_ascendente]

-----------------------------------------------------

7) VALIDACION:
Verificar si la lista final cumple:
- La primera mitad está estrictamente decreciente
- La segunda mitad está estrictamente creciente

-----------------------------------------------------

8) SALIDA:
Mostrar:
- Lista original
- Lista ordenada con mergesort
- Mitades separadas
- Lista final reconstruida
- Resultado de la validación

-----------------------------------------------------
"""

# ==========================================================
# GENERACION DE DATOS
# ==========================================================

def generar_lista(N):
    lista = []
    for i in range(1, N+1):
        valor = (i**2 + 3*i + 7) % 1000 + 50
        lista.append(valor)

    return lista


# ==========================================================
# MERGESORT
# ==========================================================

def merge(izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado += izq[i:]
    resultado += der[j:]

    return resultado


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista)//2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return merge(izquierda, derecha)


# ==========================================================
# QUICKSORT ADAPTABLE
# ==========================================================

def quicksort(lista, asc=True):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista)//2]
    menores = []
    iguales = []
    mayores = []

    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)

    if asc:
        return quicksort(menores, asc) + iguales + quicksort(mayores, asc)
    else:
        return quicksort(mayores, asc) + iguales + quicksort(menores, asc)


# ==========================================================
# VALIDACIONES
# ==========================================================

def es_decreciente(lista):
    for i in range(len(lista)-1):
        if lista[i] <= lista[i+1]:
            return False

    return True


def es_creciente(lista):
    for i in range(len(lista)-1):
        if lista[i] >= lista[i+1]:
            return False

    return True


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

# entrada
N = 0
while N < 10:
    N = int(input("Ingrese N (>=10): "))


# 1) generar lista
original = generar_lista(N)
print("Lista original:", original)


# 2) ordenar con mergesort
ordenada = mergesort(original)
print("Ordenada (mergesort):", ordenada)


# 3) obtener mediana
medio = len(ordenada)//2
mediana = ordenada[medio]


# 4) segmentar
mitad1 = []
mitad2 = []

for x in ordenada:
    if x <= mediana:
        mitad1.append(x)
    else:
        mitad2.append(x)

print("Primera mitad (<= mediana):", mitad1)
print("Segunda mitad (> mediana):", mitad2)


# 5) ordenar mitades con quicksort
mitad1_desc = quicksort(mitad1, asc=False)
mitad2_asc = quicksort(mitad2, asc=True)

print("Primera mitad descendente:", mitad1_desc)
print("Segunda mitad ascendente:", mitad2_asc)


# 6) reconstruccion
final = mitad1_desc + mitad2_asc
print("Lista final:", final)


# 7) validacion
val1 = es_decreciente(mitad1_desc)
val2 = es_creciente(mitad2_asc)

print("Primera mitad decreciente:", val1)
print("Segunda mitad creciente:", val2)

if val1 and val2:
    print("VALIDACION CORRECTA")
else:
    print("ERROR EN LA VALIDACION")