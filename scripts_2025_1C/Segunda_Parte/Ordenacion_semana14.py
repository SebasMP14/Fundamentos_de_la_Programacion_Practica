"""
Ordenar una lista significa reorganizar sus elementos 
según un criterio (por ejemplo, de menor a mayor). Esto
permite búsquedas más rápidas y facilita la visualización 
de los datos.
"""

### Selection Sort
# Selecciona repetidamente el menor (o mayor) 
# elemento y lo coloca en su posición final.
"""
def seleccion(lista, criterio): 
  n = len(lista)
  for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if criterio:
        if lista[j] < lista[min_idx]:
            min_idx = j
      else :
        if lista[j] > lista[min_idx]:
            min_idx = j
    lista[i], lista[min_idx] = lista[min_idx], lista[i]
"""
def seleccion(lista): 
  n = len(lista)
  for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if lista[j] < lista[min_idx]:
          min_idx = j
    lista[i], lista[min_idx] = lista[min_idx], lista[i]


### Insertion Sort
# Construye una lista ordenada insertando 
# un elemento a la vez en la posición correcta.
def insercion(lista):
  for i in range(1, len(lista)):
    clave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > clave:
      lista[j + 1] = lista[j]
      j -= 1
    lista[j + 1] = clave

def insercion(lista):
  print("Lista original:", lista)
  for i in range(1, len(lista)):
    clave = lista[i]
    j = i - 1
    print(f"\nInsertando {clave} en la parte ordenada {lista[:i]}")
    
    # Desplaza elementos mayores hacia la derecha
    while j >= 0 and lista[j] > clave:
      print(f"  {lista[j]} > {clave} → desplazamos {lista[j]} a la derecha")
      lista[j + 1] = lista[j]
      j -= 1
      print("  Lista intermedia:", lista)
    
    # Inserta la clave en su posición correcta
    lista[j + 1] = clave
    print(f"  Insertamos {clave} en la posición {j + 1}")
    print("  Lista después de insertar:", lista)
  
  print("\nLista ordenada:", lista)





### Buble Sort
# Recorre la lista varias veces y va moviendo 
# los elementos más grandes hacia el final.
def burbuja(lista):
  n = len(lista)
  for i in range(n):
    cambiado = False
    print(lista)
    for j in range(0, n - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        cambiado = True
    if not cambiado:
      break



# nums = list(map(int, input("Ingrese números separados por espacios: ").split()))
# seleccion(nums)
# print("Lista ordenada:", nums)



edades = [21, 18, 24, 20, 19, 23, 2, 24]
insercion(edades)
print("Edades ordenadas:", edades)



# nombres = [21, 18, 24, 20, 19, 22, 23, 24]
# burbuja(nombres)
# print("Nombres ordenados:", nombres)
