"""
UNIDAD: SUBPROGRAMAS, FUNCIONES, MÓDULOS

OBJETIVO DE LA CLASE:
- Comprender qué es un subprograma
- Definir y utilizar funciones
- Entender parámetros y valores de retorno
- Diferenciar funciones y procedimientos
- Comprender alcance de variables (scope)
- Organizar programas usando funciones
- Introducir módulos y funciones externas

"""

# ==========================================================
# 1) MOTIVACION
# ==========================================================

"""
Hasta ahora los programas son secuenciales.

Problema:
- Código repetido
- Difícil de mantener
- Poco reutilizable

Idea clave:
Dividir el problema en partes más pequeñas.

Definición:
Un subprograma es un bloque de código reutilizable
que realiza una tarea específica.

Ventajas:
- Reutilización
- Claridad
- Mantenimiento
- Abstracción
"""


# ==========================================================
# 2) DEFINICION DE FUNCIONES
# ==========================================================

"""
Sintaxis básica:

def nombre_funcion(parametros):
    instrucciones
"""

# def saludar():
#     print("Hola mundo")

# # uso de la función
# saludar()


# ==========================================================
# 3) FUNCIONES CON PARAMETROS
# ==========================================================

"""
Las funciones pueden recibir datos de entrada.
"""

# def saludar_nombre(nombre):
#     saludar = "hola 1" + nombre
#     print(saludar)
#     print("Hola", nombre)
#     return saludar

# saludo = saludar_nombre("Sebas")
# print(saludo)
# saludar_nombre("Sebas")
# saludar_nombre("Sara")


# ==========================================================
# 4) FUNCIONES CON RETORNO
# ==========================================================

"""
Las funciones pueden devolver valores usando return.
"""

# def sumar(a, b, c, d):
#     resultado = a + b + c + d
#     return int(resultado)

# x = sumar(5, 3, 5, 3.0)
# print("Resultado:", x)


# ==========================================================
# 5) DIFERENCIA: PROCEDIMIENTO vs FUNCION
# ==========================================================

"""
Procedimiento:
- No retorna valor
- Solo ejecuta acciones

Función:
- Retorna un valor
"""

# def procedimiento():
#     print("Esto es un procedimiento")

# def funcion():
#     return 10

# procedimiento()
# print(funcion())


# ==========================================================
# 6) MULTIPLES PARAMETROS Y RETORNOS
# ==========================================================

# def operaciones(a, b):
#     suma = a + b
#     resta = a - b
#     a = 5
#     return suma, resta

# suma, resta = operaciones(10, 5)
# print("Suma:", suma)
# print("Resta:", resta)
# print(a)


# ==========================================================
# 7) ALCANCE DE VARIABLES (SCOPE)
# ==========================================================

"""
Variables locales:
- Se definen dentro de una función
- No existen fuera de ella

Variables globales:
- Se definen fuera de funciones
"""

# def ejemplo_scope():
#     x = 10  # variable local
#     print("Dentro:", x)

# ejemplo_scope()

# # print(x)  # ERROR: x no existe fuera


# # ejemplo de variable global
# y = 20

# def usar_global():
#     global y
#     global a
#     a = 5
#     print("Global:", y)

# usar_global()
# print("a: ", a)


# ==========================================================
# 8) BUENAS PRACTICAS
# ==========================================================

"""
- Nombres claros
- Una función = una tarea
- Evitar funciones muy largas
- Evitar repetir código
"""

# def calcular_area_rectangulo(largo, ancho):
#     return largo * ancho

# print(calcular_area_rectangulo(5, 3))


# ==========================================================
# 9) MODULARIZACION
# ==========================================================

"""
Dividir un programa en funciones.

Ejemplo: cálculo de promedio
"""

# def leer_notas():
#     notas = []
#     for i in range(3):
#         n = float(input("Nota: "))
#         notas.append(n)
#     return notas

# def calcular_promedio(notas):
#     suma = 0
#     for n in notas:
#         suma += n
#     return suma / len(notas)

# def mostrar_resultado(promedio):
#     print("Promedio:", promedio)

# # uso
# notas = leer_notas()
# prom = calcular_promedio(notas)
# mostrar_resultado(prom)



# ==========================================================
# 10) FUNCIONES EXTERNAS (MODULOS)
# ==========================================================

"""
Python permite reutilizar código de otros archivos.

Ejemplo:
archivo: matematica.py
"""

"""
# matematica.py

def suma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b
"""

"""
Uso en otro archivo:

import matematica

print(matematica.suma(2,3))
"""

# import funciones

# print("suma: ", funciones.suma(5, 10))


# ==========================================================
# 11) IMPORTACION SELECTIVA
# ==========================================================

"""
from modulo import funcion
"""

"""
from matematica import suma

print(suma(5,2))
"""

# a = 20
# from funciones import multiplicar, a

# multiplicacion2 = multiplicar(10.1, 10, 10)
# print("multiplicación: ", multiplicacion2, "a: ", a)
# print("multiplicación: ", mult, "a: ", a)



# ==========================================================
# 12) MODULOS ESTANDAR
# ==========================================================

"""
Ejemplo: math
"""

# import math
# # math.
# print(math.sqrt(16))
# print(math.pi)


# ==========================================================
# 13) EJERCICIO INTEGRADOR
# ==========================================================

"""
Problema:
Crear un programa modular que:

1) Lea N números
2) Determine:
    - mayor
    - menor
    - promedio
3) Mostrar resultados usando funciones
"""
# def leer_numeros():
#     n = int(input("Cantidad: "))
#     numeros = []

#     for i in range(n):
#         numeros.append(float(input("Numero: ")))

#     return numeros

# def calcular_mayor(numeros):
#     mayor = numeros[0]

#     for n in numeros:
#         if n > mayor:
#             mayor = n

#     return mayor

# def calcular_menor(numeros):
#     menor = numeros[0]

#     for n in numeros:
#         if n < menor:
#             menor = n

#     return menor

# def calcular_promedio(numeros):
#     suma = 0

#     for n in numeros:
#         suma += n

#     return suma / len(numeros)

# def mostrar(mayor, menor, promedio):
#     print("Mayor:", mayor)
#     print("Menor:", menor)
#     print("Promedio:", promedio)

# # programa principal
# datos = leer_numeros()
# may = calcular_mayor(datos)
# men = calcular_menor(datos)
# prom = calcular_promedio(datos)

# mostrar(may, men, prom)




############################################################################

"""
Se desea analizar una serie de números enteros positivos.

El programa debe:

1) Solicitar un número N (validar: entero positivo).
2) Para cada uno de los N números:
    - Leer un número entero positivo.
    - Convertirlo manualmente a base 2 (binario) SIN usar funciones de Python como bin().
    - Contar:
        a) cantidad de unos en su representación binaria
        b) cantidad de ceros en su representación binaria
    - Determinar si la cantidad de unos es un número PRIMO.

3) Al finalizar, determinar:
    - cuál número tiene mayor cantidad de ceros en su representación binaria
    - cuántos números tienen cantidad de unos PRIMA

4) Mostrar:
    - resultados individuales por número
    - resultados globales

RESTRICCIONES:
- NO usar strings
- NO usar listas
- SOLO usar variables, ciclos, condicionales y funciones
- Se debe implementar:
    - conversión a binario
    - conteo de bits
    - verificación de número primo

EJEMPLO CONCEPTUAL:

Entrada:
N = 3
6
10
7

Proceso:
6  -> 110  -> ceros: 1, unos: 2 (2 es primo)
10 -> 1010 -> ceros: 2, unos: 2 (2 es primo)
7  -> 111  -> ceros: 0, unos: 3 (3 es primo)

Salida esperada:
Numero: 6  Ceros: 1  Unos: 2  (PRIMO)
Numero: 10 Ceros: 2  Unos: 2  (PRIMO)
Numero: 7  Ceros: 0  Unos: 3  (PRIMO)

Mayor cantidad de ceros: 2 (Numero: 10)
Cantidad de numeros con unos primos: 3
"""

# def es_entero(cadena):
#     if len(cadena) == 0:
#         return False

#     i = 0

#     # permitir signo negativo
#     if cadena[0] == '-':
#         if len(cadena) == 1:
#             return False
#         i = 1

#     for j in range(i, len(cadena)):
#         if cadena[j] < '0' or cadena[j] > '9':
#             return False

#     return True

# def validar_entero_en_rango(mensaje, minimo, maximo):
#     while True:
#         entrada = input(mensaje)

#         if not es_entero(entrada):
#             print("Error: debe ingresar un numero entero")
#         else:
#             numero = int(entrada)

#             if numero < minimo or numero > maximo:
#                 print("Error: el numero debe estar entre", minimo, "y", maximo)
#             else:
#                 return numero

# # x = validar_entero_en_rango("Ingrese un numero entre -5 y 5: ", -5, 5)
# # print("Numero valido:", x)

# # ==========================================================
# # FUNCION: CONTAR CEROS Y UNOS EN BINARIO (SIN STRING)
# # ==========================================================

# def contar_bits(numero):
#     ceros = 0
#     unos = 0

#     while numero > 0:
#         resto = numero % 2

#         if resto == 0:
#             ceros += 1
#         else:
#             unos += 1

#         numero = numero // 2

#     return ceros, unos

# # ==========================================================
# # FUNCION: VERIFICAR SI UN NUMERO ES PRIMO
# # ==========================================================

# def es_primo(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# # ==========================================================
# # PROGRAMA PRINCIPAL
# # ==========================================================

# # Validación de N

# N = validar_entero_en_rango("Ingrese N (cant de nums): ", 1, 5)

# mayor_ceros = -1
# numero_mayor_ceros = 0

# contador_primos = 0


# for i in range(N):
#     num = validar_entero_en_rango(f"Ingrese el numero {i+1}: ", 1, 1000)

#     ceros, unos = contar_bits(num)
#     primo = es_primo(unos)
#     print("Numero:", num, "Ceros:", ceros, "Unos:", unos, end=" ")

#     if primo:
#         print("(PRIMO)")
#         contador_primos += 1
#     else:
#         print("(NO PRIMO)")

#     # determinar el numero con mas ceros
#     if ceros > mayor_ceros:
#         mayor_ceros = ceros
#         numero_mayor_ceros = num


# print("Mayor cantidad de ceros:", mayor_ceros, "(Numero:", numero_mayor_ceros, ")")
# print("Cantidad de numeros con unos primos:", contador_primos)