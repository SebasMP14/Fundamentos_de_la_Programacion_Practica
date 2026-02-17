# Clase 2 - semana 3
# radio = 5
# area = pi * radio ** 2
# 78.54 --> print(area)

entero = 10 # 10 -10 0
real = 3.14 # -0.5 0.0 0.5
texto = "programación" # "N palabras" "1234%^&$#" "True y falso"
booleano = True # True False

print(type(10))
print(type(3.14))
print(type("programación"))
print(type(True))

print(entero)
print(real)
print(texto)
print(booleano)
# print(type(entero))
# print(type(real))
# print(type(texto))
# print(type(booleano))
"""
Una variable es un espacio en memoria que se reserva 
para almacenar un valor.
El tipo de dato de una variable determina el tipo de 
valor que puede almacenar y las operaciones que se 
pueden realizar con ella.
"""
edad = 20
print(edad)

edad = 21
print(edad)


a = 10
b = 5

resultado = a + b # suma

print(resultado)
resultado = a - b # resta
print(resultado)
resultado = a * b # multiplicación
print(resultado)
resultado = a / b # división
print(resultado)
resultado = a // b # división entera
print(resultado)
resultado = a % b # módulo o resto de la división
print(resultado) 
resultado = a ** b # potencia
print(resultado)
resultado = a + b * 2
print(resultado) # 10 + 5 * 2 = 10 + 10 = 20
resultado = (a + b) * 2
print(resultado) # (10 + 5) * 2 = 15 * 2 = 30


"""
Entrada de datos: input()
Salida de datos: print()
"""
nombre = input("Ingrese su nombre: ")

print(nombre)
edad = input("Ingrese su edad: ")
print(type(edad))



edad = input("Ingrese su edad: ")

edad = int(edad)

print(type(edad))

###############################33

numero1 = input("Ingrese numero: ")
numero2 = input("Ingrese numero: ")

numero1 = int(numero1)
numero2 = int(numero2)

suma = numero1 + numero2

print(suma)


print("10" + "5")


año = input("Ingrese su año de nacimiento: ")
año = int(año)
edad = 2026 - año
print("Hola", nombre)
print("Su edad es", edad)



"""
Escriba un programa que solicite al usuario el 
el largo y ancho de un rectángulo y mostrar el área.
"""


"""
Un vehículo recorre una cierta distancia y consume una determinada 
cantidad de combustible.

Escriba un programa en Python que:
Solicite al usuario su nombre, la distancia recorrida en kilómetros (float) y la 
cantidad de combustible consumido en litros (int)

Calcule el consumo de combustible, definido como:
consumo=distancia/combustible

Muestre como salida el nombre del usuario y el consumo calculado

Se espera algo como:
Ingrese su nombre: Sebas
Ingrese la distancia recorrida (km): 150
Ingrese el combustible consumido (litros): 10

Usuario: Sebas
Consumo: 15.0 km/l
"""


"""
El IMC se calcula como:

IMC=peso/altura**2

Solicitar:
nombre
peso en kg
altura en metros
"""