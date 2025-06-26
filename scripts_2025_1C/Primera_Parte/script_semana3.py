#######################################
# Pide al usuario su edad y verifica si puede votar 
# (mayor o igual a 18 años).

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")





#######################################
# Pide al usuario un número entero e indica si es
# par o impar.

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")








#######################################
# Pide al usuario un número e indica si
# está entre 10 y 20, inclusive.

numero = float(input("Ingresa un número: "))

if 10 <= numero <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está en el rango.")

if (10 <= numero) and (numero <= 20):
    print("Si")
else: 
    print("No")





numero = int(input())
print(numero)


#######################################
# Define un número secreto y pide al usuario 
# que lo adivine.

numero_secreto = 7
adivina = int(input("Adivina el número secreto (entre 1 y 10): "))

if adivina == numero_secreto:
    print("¡Correcto! Has adivinado el número.")
else:
    print("Incorrecto. Intenta de nuevo.")

# Variacion, adivina el numero generado 
# aleatoriamente.

import random as r

numero_secreto = r.randint(0, 10)  # Genera un número aleatorio entre 0 y 10
adivina = int(input("Adivina el número secreto (entre 0 y 10): "))

if adivina == numero_secreto:
    print("¡Correcto! Has adivinado el número.")
else:
    print(f"Incorrecto. El número secreto era {numero_secreto}.")








#################################################
# Pide al usuario su calificación y clasifícala en:
#  A (90-100), B (80-89), C (70-79), D (60-69) o F (<60).

nota = float(input("Ingresa tu calificación: "))

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota > 60:
    print("Calificación: D")
else:
    print("Calificación: F")





################################################
# Pide al usuario tres números e indica si todos son positivos.

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > 0 and b > 0 and c > 0:
    print("Todos los números son positivos.")
    
elif a == 0 or b == 0 or c == 0:
    print("Al menos un nro es cero")
else:
    if a < 0: 
        print("a es negativo", a)
    elif b < 0:
        print("b es negativo", b)
    else:
        print("c es negativo", c)