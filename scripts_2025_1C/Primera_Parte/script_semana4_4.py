"""
Dada una lista de frases, contar cuántas veces aparece cada 
palabra en un diccionario.
"""

frases = ["hola mundo", "mundo Python", "hola Python mundo"]
frecuencia = {}

for frase in frases:
    palabras = frase.split()
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

print("Frecuencia de palabras:", frecuencia)


"""
Dada una lista de números, encontrar el número que más veces aparece y cuántas veces se repite.
"""
numeros = [3, 1, 4, 1, 2, 3, 1, 4, 4, 4, 2, 3, 3]
conteo = {}

for num in numeros:
    conteo[num] = conteo.get(num, 0) + 1

max_repetido = max(conteo, key=conteo.get)
print(f"El número más repetido es {max_repetido} con {conteo[max_repetido]} apariciones.")


"""
Dada una tupla de palabras, obtener una lista solo con las palabras que no están repetidas.
"""
palabras = ("python", "codigo", "python", "ejercicio", "codigo", "programar")
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

unicas = [palabra for palabra in palabras if conteo[palabra] == 1]
print("Palabras únicas:", unicas)


"""
Dado un diccionario de estudiantes, buscar un nombre y usar una bandera para indicar si fue encontrado.
"""
estudiantes = [
    {"nombre": "Ana", "edad": 20, "carrera": "Informática"},
    {"nombre": "Luis", "edad": 22, "carrera": "Electrónica"},
    {"nombre": "Sofía", "edad": 21, "carrera": "Mecatrónica"}
]

buscado = input("Ingrese el nombre del estudiante: ")
encontrado = False

for estudiante in estudiantes:
    if estudiante["nombre"] == buscado:
        print("Estudiante encontrado:", estudiante)
        encontrado = True
        break  # Si lo encuentra, ya no sigue buscando

if not encontrado:
    print("Estudiante no encontrado.")



"""
Sistema de registro de ventas de una tienda. Se tiene una lista de ventas donde cada venta es una tupla (producto, cantidad). Se debe:

Guardar en un diccionario la cantidad total vendida de cada producto.
Identificar el producto más vendido usando una bandera.
"""
ventas = [
    ("manzana", 3), ("banana", 2), ("manzana", 5), 
    ("pera", 4), ("banana", 1), ("pera", 2), ("manzana", 2)
]

registro_ventas = {}

for producto, cantidad in ventas:
    if producto in registro_ventas:
        registro_ventas[producto] += cantidad
    else:
        registro_ventas[producto] = cantidad

# Encontrar el producto más vendido
producto_mas_vendido = None
max_cantidad = 0

for producto, cantidad in registro_ventas.items():
    if cantidad > max_cantidad:
        max_cantidad = cantidad
        producto_mas_vendido = producto

print("Registro de ventas:", registro_ventas)
print(f"El producto más vendido es '{producto_mas_vendido}' con {max_cantidad} unidades.")
