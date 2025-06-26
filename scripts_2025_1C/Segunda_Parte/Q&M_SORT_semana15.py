"""
QuickSort: 
- Se elige un elemento como pivote.
- Se divide la lista en dos partes: los elementos menores que 
el pivote y los mayores o iguales al pivote.
- Se aplica quicksort recursivamente a las dos partes.
- Se combinan los resultados.

Tiempo de ejecución: 
  Mejor caso (lista bien equilibrada): O(n log n)
  Peor caso (lista ya ordenada o pivote mal elegido): O(n²)
  Caso promedio: O(n log n)
"""
def quicksort(lista):
  if len(lista) <= 1:
    return lista
  else:
    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    mayores = [x for x in lista[1:] if x >= pivote]
    print("Menores: ", menores)
    print("Pivote: ", pivote)
    print("Mayores: ", mayores)
    print("---")
    return quicksort(menores) + [pivote] + quicksort(mayores)

# nums = [8, 3, 1, 7, 0, 10, 2]
# ordenados = quicksort(nums)
# print(ordenados)


"""
MergeSort: 
- Divide la lista en dos mitades.
- Ordena recursivamente ambas mitades.
- Combina (merge) ambas listas ordenadas en una sola.

Tiempo de ejecución:
  Siempre: O(n log n)
  Necesita memoria adicional proporcional a n.
"""
def mergesort(lista):
  if len(lista) <= 1:
    return lista
  medio = len(lista) // 2
  izquierda = mergesort(lista[:medio])
  derecha = mergesort(lista[medio:])
  print("izquierda: ", izquierda)
  print("derecha: ", derecha)
  print("---")
  return merge(izquierda, derecha)

def merge(izq, der):
  resultado = []
  i = j = 0
  while i < len(izq) and j < len(der):
    print(resultado)
    if izq[i] < der[j]:
      resultado.append(izq[i])
      i += 1
    else:
      resultado.append(der[j])
      j += 1
  resultado.extend(izq[i:])
  resultado.extend(der[j:])
  return resultado

nums = [8, 3, 1, 7, 0, 10, 2]
print(nums)
ordenados = mergesort(nums)
print(ordenados)
