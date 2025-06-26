#############################################
# Pide al usuario tres longitudes de lados y determina 
# si forman un triángulo válido. 
# Si es válido, clasifica el triángulo como equilátero, 
# isósceles o escaleno.

#obs: "c" no puede ser mayor o igual a la suma de 
# "a" y "b" pa que sea un triang...
a = float(input("Ingresa el primer lado: "))
b = float(input("Ingresa el segundo lado: "))
c = float(input("Ingresa el tercer lado: "))

if a < 0 or b < 0 or c < 0:
    print("uno de los valores ingresados es negativo")
elif a + b > c or a + c > b or b + c > a:
    if a == b == c: # EJEMPLO DE ESTRUCTURA ANIDADA
        print("Es un triángulo equilátero.")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("No es un triángulo válido.")





################################################
# Crea un juego donde el usuario elige piedra, papel o tijera, 
# y la computadora elige aleatoriamente una opción. 
# Determina quién gana.

import random

opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

usuario = input("Elige piedra, papel o tijera: ")

print("Computadora eligió:", computadora)

if usuario == computadora:
    print("Empate.")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")




#################################################
# Pide al usuario un carácter y determina si es una vocal, 
# una consonante, un número o un símbolo.

caracter = input("Ingresa un solo carácter: ")

if caracter.isdigit():
    print("Es un número.")
elif caracter.isalpha():
    if caracter.lower() in "aeiou":
        print("Es una vocal.")
    else:
        print("Es una consonante.")
else:
    print("Es un símbolo.")







#######################################
# Pide tres números al usuario y determina el mayor 
# sin usar la función max().

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

if a >= b and a >= c:
    print("El mayor es:", a)
elif b >= a and b >= c:
    print("El mayor es:", b)
else:
    print("El mayor es:", c)





####################################
# Determine si un numero es primo

num = int(input("Ingresa un número entero: "))

if num > 1:
    es_primo = True
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo.")
    else:
        print("No es un número primo.")
else:
    print("No es un número primo.")







##################################
# Un sistema de semáforos inteligente ajusta el tiempo de luz 
# verde según la cantidad de vehículos en cada dirección. 
# Escribe un programa que:

# Pida al usuario el número de vehículos en la dirección Norte-Sur 
# y Este-Oeste.

# Si una dirección tiene más del doble de vehículos que la otra, 
# esa dirección obtiene 60 segundos de luz verde y la otra 
# 30 segundos.

# Si el tráfico es similar (menos del doble de diferencia), 
# ambas direcciones obtienen 45 segundos de luz verde.

# Usa operadores lógicos y relacionales para determinar la 
# configuración correcta.
ns = int(input("Número de vehículos Norte-Sur: "))
ew = int(input("Número de vehículos Este-Oeste: "))

if ns > 2 * ew:
    print("Norte-Sur: 60s, Este-Oeste: 30s")
elif ew > 2 * ns:
    print("Este-Oeste: 60s, Norte-Sur: 30s")
else:
    print("Norte-Sur: 45s, Este-Oeste: 45s")
