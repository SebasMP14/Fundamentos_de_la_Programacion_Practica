"""
Búsqueda lineal: Se recorre la lista elemento por elemento 
hasta encontrar el valor buscado o llegar al final de la lista.

Empezamos desde el primer elemento.
Comparamos cada elemento con el valor que queremos encontrar.
Si encontramos una coincidencia, devolvemos su posición.
Si llegamos al final y no lo encontramos, devolvemos una señal (por ejemplo -1).

###################

Búsqueda Binaria: Divide la lista ordenada por la mitad en cada 
paso para reducir la búsqueda a la mitad del tamaño actual. 
(OBS: LA lista debe estar ordenada...)
Se calcula el índice del elemento del medio.

Se compara el valor medio con el objetivo:
Si es igual, se ha encontrado
Si el objetivo es menor, buscamos en la mitad izquierda.
Si es mayor, buscamos en la mitad derecha.

Se repite el proceso hasta encontrarlo o hasta que el rango sea inválido.
"""


"""
Buscar un número en una lista
"""
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        print(f"indice: {i}, valor: {lista[i]}")
        if lista[i] == objetivo:
            return i  # Retorna la posición
    return -1  # No encontrado

lista = [4, 7, 2, 9, 5]
print(busqueda_lineal(lista, 9))

"""
Buscar todos los multiplos de 3
"""
def buscar_multiplos(lista):
    resultado = []
    for elem in lista:
        print(f"elem: {elem}")
        if elem % 3 == 0:
            resultado.append(elem)
    return resultado

def buscar_multiplosi(lista):
    resultado = []
    for i in range(len(lista)):
        print(f"elem: {lista[i]}")
        if lista[i] % 3 == 0:
            resultado.append(i)
    return resultado

lista = [5, 9, 12, 7, 18]
print(buscar_multiplosi(lista))  


"""
Búsqueda binaria
"""
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"izq: {izquierda}, der: {derecha}")
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista = [2, 4, 6, 8, 10, 12]
print(busqueda_binaria(lista, 10)) 




################# Implementación recursiva
def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha: # No se encontró el objetivo
        return -1
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)

lista = [1, 3, 5, 7, 9, 11]
print(busqueda_binaria_recursiva(lista, 3, 0, len(lista)-1))




"""
Comparación y tiempos de ejecución
"""
import time

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

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

# Crear una lista grande
lista = list(range(1_000_000))
objetivo = 999_999

# Medir tiempo de búsqueda lineal
inicio = time.time()
busqueda_lineal(lista, objetivo)
print("Lineal:", time.time() - inicio)

# Medir tiempo de búsqueda binaria
inicio = time.time()
busqueda_binaria(lista, objetivo)
print("Binaria:", time.time() - inicio)



"""
Búsqueda de un nro que no está en la lista
"""
objetivo = -5  # No está en la lista

# Repetimos pruebas con este nuevo objetivo
inicio = time.time()
busqueda_lineal(lista, objetivo)
print("Lineal (no encontrado):", time.time() - inicio)

inicio = time.time()
busqueda_binaria(lista, objetivo)
print("Binaria (no encontrado):", time.time() - inicio)
