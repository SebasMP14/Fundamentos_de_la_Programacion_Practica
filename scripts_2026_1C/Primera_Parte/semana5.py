# """ UNIDAD: Estructuras de datos básicas en Python. Secuencias, 
# cadenas, tuplas y listas. Diccionarios. Arreglos Estructuras 
# repetitivas """

# #########################################
# # Cadena o String
# nombre = "Sejdvjenv"

# Acceso por índice
# print(nombre[0])  # S
# print(nombre[1])  # e

# # Error intencional: índice fuera de rango
# print(nombre[4])  # IndexError

# # # Longitud de la cadena
# print(len(nombre))

# # # Recorrido de una cadena
# for letra in nombre:
#     print(letra)

# # # Concatenación
# apellido = "Monje"
# completo = nombre + " " + apellido
# print(completo)

# # # Repetición
# print(nombre * 3)

# # # Métodos útiles de string
# print(nombre.upper())

# print(nombre.lower())
# print(nombre.startswith("Se"))
# print("A" in nombre)  # operador de pertenencia

# #########################################
# # Listas
# """
# Una lista es una secuencia MUTABLE.
# Puede modificarse después de creada.
# Permite almacenar múltiples valores de distintos tipos.
# """

# notas = [80, 75, 90]

# # Acceso por índice
# print(notas[0])
# print(notas)
# # Modificación
# notas[-1] = 85
# print(notas)
# # Agregar elemento
# notas.append(90)
# print(notas)

# # # Insertar en posición específica
# notas.insert(1, 90)
# print(notas)

# # # Eliminar elemento
# notas.remove(90)
# print(notas)

# # Longitud
# print(len(notas))

# # Recorrido
# for nota in notas:
#     print(nota)

# # # Sumar elementos (acumulador)
# suma = 0
# for nota in notas:
#     suma = suma + nota
# print(suma)

# print("Suma:", suma)

# # Promedio
# promedio = suma / len(notas)
# print("Promedio:", promedio)

# # # Verificar si elemento existe
# print(85 in notas)

# range
# r = range(-1, 7, 2)

# print(r)            # objeto range
# print(type(r))      # <class 'range'>

# # Convertir a lista para visualizar
# print(list(r))

#########################################
# Tuplas (datos fijos o configuraciones)
# punto = (3, 4)

# print(punto[0]) # 3
# print(punto[1]) # 4

# Error intencional: no se puede modificar
# punto[0] = 5  # TypeError

# Recorrido
# for valor in punto:
#     print(valor)

# # Tupla de configuración
# configuracion = ("localhost", 8080, True)

#########################################
# # Diccionarios
# estudiante = {
#     "nombre": "Ana",
#     "edad": 20,
#     "nota": 85
# }

# # Acceso por clave
# # print(estudiante["nombre"])

# # Modificar valor
# estudiante["nota"] = 90

# # Agregar nuevo par clave:valor
# estudiante["carrera"] = "Ingenieria"

# # Recorrer claves
# for clave in estudiante:
#     print(clave, estudiante[clave])

# # Métodos útiles
# print(estudiante.keys())
# print(estudiante.values())
# print(estudiante.items())

# # Verificar si clave existe
# print("edad" in estudiante)

# #########################################
# # Arreglos
# """
# En Python, las listas funcionan como arreglos dinámicos.

# Características:
# - Pueden cambiar de tamaño.
# - Permiten almacenar múltiples elementos del mismo tipo o 
# diferentes tipos.

# En ingeniería tradicional, un arreglo:
# - Es una estructura homogénea.
# - Tamaño fijo."""


# #########################################
# ### Ciclos Repetitivos
# # Ciclos While
# """
# El ciclo while repite mientras una condición sea verdadera.
# Debe evitarse el ciclo infinito.
# """

# contador = 0

# while contador <= 5:
#     print("Contador:", contador)
#     contador = contador + 1  # IMPORTANTE actualizar

# # Ejemplo clásico: validación
# numero = -1

# while numero < 0:
#     numero = int(input("Ingrese numero positivo: "))

# # while True:
# #     numero = int(input("Ingrese numero positivo: "))
# #     if numero >= 0:
# #         break

# while True:
#     print("holaaa")
#     break

# #########################################
# # Ciclos for
# """
# El ciclo for recorre secuencias.
# Es ideal para listas, cadenas, tuplas.
# """

# numeros = [10, 20, 30, 40]

# for n in numeros:
#     print(n)

# # Uso con range()
# for i in range(5):
#     print(i)

# range(inicio, fin)
# for i in range(2, 6):
#     print(i)

# range(inicio, fin, paso)
# for i in range(0, 11, 2):
#     print(i)




# ###########################################################
# ###########################################################
# # Ejercicios
# """
# Problema:
# Almacenar 5 temperaturas.
# Determinar:
# - Máxima
# - Mínima
# - Promedio
# Realizar el algoritmo sólo con ciclos while
# """

# temperaturas = []

# for i in range(5):
#     t = float(input("Ingrese temperatura: "))
#     temperaturas.append(t)
#     print(temperaturas)

# maxima = temperaturas[0]
# minima = temperaturas[0]
# suma = 0

# for t in temperaturas:
#     if t > maxima:
#         maxima = t
    
#     if t < minima:
#         minima = t
    
#     suma = suma + t

# promedio = suma / len(temperaturas)

# print("Maxima:", maxima)
# print("Minima:", minima)
# print("Promedio:", promedio)












# """Sistema básico de gestión de estudiantes.

# El programa debe:

# 1) Permitir ingresar N estudiantes (N definido por el usuario).
# 2) Para cada estudiante:
#       - nombre
#       - carrera
#       - 3 notas
# 3) Almacenar la información en una estructura adecuada.
# 4) Calcular para cada estudiante:
#       - promedio
#       - condición (Aprobado si promedio >= 60, caso contrario Reprobado)
# 5) Determinar:
#       - promedio general del curso
#       - estudiante con mayor promedio
#       - estudiante con menor promedio
# 6) Mostrar un resumen final estructurado.

# RESTRICCIONES:
# - No usar funciones.
# - No usar librerías externas.
# - No usar estructuras avanzadas aún no vistas.
# - Solo usar lo desarrollado hasta ahora.
# """

cantidad = int(input("Ingrese cantidad de estudiantes: "))

estudiantes = []   # Lista que almacenará diccionarios

for i in range(cantidad):

    print("\nEstudiante", i + 1)

    nombre = input("Nombre: ")
    carrera = input("Carrera: ")

    notas = []

    for j in range(3):
        nota = float(input("Ingrese nota: "))
        notas.append(nota)

    # Calcular promedio individual
    suma = 0
    for n in notas:
        suma += n

    promedio = suma / len(notas)

    # Determinar condición
    if promedio >= 60:
        condicion = "Aprobado"
    else:
        condicion = "Reprobado"

    # Crear diccionario del estudiante
    estudiante = {
        "nombre": nombre,
        "carrera": carrera,
        "notas": notas,
        "promedio": promedio,
        "condicion": condicion
    }

    estudiantes.append(estudiante)
    print(estudiantes)

promedio_general = 0

mayor_promedio = estudiantes[0]["promedio"]
# valor_0 = estudiantes[0]["notas"][0]
menor_promedio = estudiantes[0]["promedio"]

mejor_estudiante = estudiantes[0]["nombre"]
peor_estudiante = estudiantes[0]["nombre"]

for est in estudiantes:

    promedio_general = promedio_general + est["promedio"]

    if est["promedio"] > mayor_promedio:
        mayor_promedio = est["promedio"]
        mejor_estudiante = est["nombre"]

    if est["promedio"] < menor_promedio:
        menor_promedio = est["promedio"]
        peor_estudiante = est["nombre"]

promedio_general = promedio_general / len(estudiantes)

print("\n========== REPORTE FINAL ==========\n")

for est in estudiantes:
    print("Nombre:", est["nombre"])
    print("Carrera:", est["carrera"])
    print("Notas:", est["notas"])
    print("Promedio:", est["promedio"])
    print("Condición:", est["condicion"])
    print("----------------------------------")

print("\nPromedio general del curso:", promedio_general)
print("Mejor estudiante:", mejor_estudiante, "-", mayor_promedio)
print("Peor estudiante:", peor_estudiante, "-", menor_promedio)











# """
# Una planta tiene varios sensores que registran temperatura.

# El programa debe:

# 1) Solicitar la cantidad de sensores.
# 2) Para cada sensor ingresar:
#       - ID del sensor
#       - ubicación (sector)
#       - 5 mediciones de temperatura
# 3) Almacenar toda la información correctamente estructurada.
# 4) Para cada sensor calcular:
#       - temperatura promedio
#       - temperatura máxima
#       - temperatura mínima
#       - estado:
#             "ALERTA" si alguna medición supera 80 grados
#             "NORMAL" en caso contrario
# 5) Determinar:
#       - sensor con mayor promedio
#       - sensor con menor promedio
#       - promedio general de la planta
# 6) Permitir buscar un sensor por ID y mostrar su información.
# 7) Mostrar reporte final completo.

# RESTRICCIONES:
# - No usar funciones.
# - No usar librerías externas.
# - Solo usar estructuras vistas hasta ahora.
# """



























# cantidad = int(input("Ingrese cantidad de sensores: "))

# sensores = []   # Lista de diccionarios

# for i in range(cantidad):

#     print("\nSensor", i + 1)

#     sensor_id = input("ID del sensor: ")
#     ubicacion = input("Ubicacion: ")

#     mediciones = []
#     alerta = False

#     for j in range(5):
#         temp = float(input("Ingrese temperatura: "))
#         mediciones.append(temp)

#         if temp > 80:
#             alerta = True

#     # Calcular estadísticas
#     suma = 0
#     maxima = mediciones[0]
#     minima = mediciones[0]

#     for t in mediciones:
#         suma = suma + t

#         if t > maxima:
#             maxima = t

#         if t < minima:
#             minima = t

#     promedio = suma / len(mediciones)

#     if alerta:
#         estado = "ALERTA"
#     else:
#         estado = "NORMAL"

#     sensor = {
#         "id": sensor_id,
#         "ubicacion": ubicacion,
#         "mediciones": mediciones,
#         "promedio": promedio,
#         "maxima": maxima,
#         "minima": minima,
#         "estado": estado
#     }

#     sensores.append(sensor)

# promedio_general = 0

# mayor_promedio = sensores[0]["promedio"]
# menor_promedio = sensores[0]["promedio"]

# sensor_mayor = sensores[0]["id"]
# sensor_menor = sensores[0]["id"]

# for s in sensores:

#     promedio_general = promedio_general + s["promedio"]

#     if s["promedio"] > mayor_promedio:
#         mayor_promedio = s["promedio"]
#         sensor_mayor = s["id"]

#     if s["promedio"] < menor_promedio:
#         menor_promedio = s["promedio"]
#         sensor_menor = s["id"]

# promedio_general = promedio_general / len(sensores)

# buscar = input("\nIngrese ID de sensor a buscar: ")

# encontrado = False

# for s in sensores:
#     if s["id"] == buscar:
#         print("\n--- SENSOR ENCONTRADO ---")
#         print("ID:", s["id"])
#         print("Ubicacion:", s["ubicacion"])
#         print("Mediciones:", s["mediciones"])
#         print("Promedio:", s["promedio"])
#         print("Maxima:", s["maxima"])
#         print("Minima:", s["minima"])
#         print("Estado:", s["estado"])
#         encontrado = True

# if not encontrado:
#     print("Sensor no encontrado.")

# print("\n========== REPORTE GENERAL ==========\n")

# for s in sensores:
#     print("ID:", s["id"])
#     print("Ubicacion:", s["ubicacion"])
#     print("Estado:", s["estado"])
#     print("Promedio:", s["promedio"])
#     print("----------------------------------")

# print("Promedio general planta:", promedio_general)
# print("Sensor con mayor promedio:", sensor_mayor, "-", mayor_promedio)
# print("Sensor con menor promedio:", sensor_menor, "-", menor_promedio)