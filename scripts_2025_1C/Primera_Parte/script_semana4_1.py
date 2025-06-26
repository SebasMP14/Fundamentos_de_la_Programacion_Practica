"""
Pedir al usuario un número N y calcular la suma de los 
primeros N números naturales usando una lista.
Usar sum(lista) para obtener el resultado.
"""
N = int(input("Ingrese un número N: "))
numeros = list(range(1, N+1))
suma = sum(numeros)

print(f"La suma de los primeros {N} números es: {suma}")




"""
Crear un diccionario donde las claves sean los
 números del 1 al 5 y los valores sean sus cuadrados.
Usar un for para generar las claves y valores.
"""
cuadrados = {num: num**2 for num in range(1, 6)}
print("Diccionario de cuadrados:", cuadrados)

cuadrados = {}
for num in range(1, 6):
    cuadrados[num] = num**2
print(cuadrados)


"""
Dada una tupla fija de nombres (("Ana", "Juan", "Luis", "Pedro")), 
pedir al usuario un nombre y verificar si está en la tupla.
Usar un for y una bandera para indicar si el nombre fue encontrado.
"""
nombres = ("Ana", "Juan", "Luis", "Pedro")
buscado = input("Ingrese un nombre a buscar: ")

encontrado = False
for nombre in nombres:
    print(nombre)
    if nombre == buscado:
        encontrado = True
        # break

if encontrado:
    print(f"{buscado} está en la tupla.")
else:
    print(f"{buscado} no está en la tupla.")



"""
Crear una lista de listas (matriz) de tamaño 3x3 con los primeros números pares.
Usar listas por comprensión o for anidados.
"""
matriz = [[(fila * 3 + col) * 2 for col in range(3)] for fila in range(3)]

print("Matriz de números pares:")
for fila in matriz:
    print(fila)


lista = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# for fila in range(3):
#     for columna in range(3):
#         print(lista[fila][columna])

for fila in lista:
    for valor in fila:
        print(valor)