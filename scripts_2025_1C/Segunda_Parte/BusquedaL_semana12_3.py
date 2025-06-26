
"""
Buscar el índice de un número usando np.where
"""
import numpy as np

def buscar_lineal_np(arr, objetivo):
    indices = np.where(arr == objetivo)[0]
    if indices.size > 0:
        return indices[0]  # Primer índice encontrado
    else:
        return -1

arr = np.array([10, 20, 30, 40, 50])
print(buscar_lineal_np(arr, 30))  
print(buscar_lineal_np(arr, 99))  


"""
Buscar posición de inserción con np.searchsorted
"""
import numpy as np

def buscar_binaria_np(arr, objetivo):
    idx = np.searchsorted(arr, objetivo)
    if idx < len(arr) and arr[idx] == objetivo:
        return idx
    return -1


arr = np.array([5, 10, 15, 20, 25])
print(buscar_binaria_np(arr, 15))  
print(buscar_binaria_np(arr, 13))  



import numpy as np

lista = [3, 1, 4, 2]
ordenada = np.sort(lista) # → ordena
print(ordenada)  # → [1 2 3 4]

arr = np.array([3, 1, 4, 2])
ordenado = np.sort(arr)
print(ordenado)  # → [1 2 3 4]
