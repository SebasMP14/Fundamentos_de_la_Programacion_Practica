"""Escribir un programa que reciba un número entero y 
sume sus dígitos repetidamente hasta obtener un solo dígito.

Ejemplo:
Entrada: 9875
Proceso: 9 + 8 + 7 + 5 = 29 → 2 + 9 = 11 → 1 + 1 = 2
Salida: 2
"""
# //correo: amonje@fiuna.edu.py
n = int(input("Ingrese un número: "))

while n >= 10:  # Mientras tenga más de un dígito
    suma = 0
    while n > 0:
        print(suma)
        suma += n % 10  # Extraer y sumar el último dígito
        print(suma)
        n //= 10        # Eliminar el último dígito
        print("n: ", n)
    n = suma  # Asignar la suma como nuevo número

print("Dígito final:", n)



"""
Dado un número entero positivo, invertir el orden de sus 
dígitos sin usar cadenas (str).

Ejemplo:
Entrada: 1234
Salida: 4321
"""
#entrada 147
n = int(input("Ingrese un número para invertir: "))
numero_invertido = 0

while n > 0:
    digito = n % 10  # Extraer el último dígito
    print(digito)
    numero_invertido = numero_invertido * 10 + digito  # Construir número invertido
    print(numero_invertido)
    n //= 10  # Eliminar el último dígito
    print(n)

print("Número invertido:", numero_invertido)
#################################
"""Escriba un programa que lea un número entero desde el teclado (validar) e imprima 
por pantalla dicho número con sus dígitos invertidos. El número puede ser positivo o 
negativo, y la inversión debe respetar el signo original del número.
Ejemplo:
-123456

Salida:
-654321

Requisitos:
No utilice funciones predefinidas que inviertan cadenas o listas directamente
 (por ejemplo, [::-1] o reverse()).
Asegúrese de conservar correctamente el signo del número.
El programa debe validar que la entrada sea un número entero. Si la entrada no
 es válida, se debe imprimir:
Error: entrada no válida"""









"""
Dado un número entero positivo, aplicar la secuencia de Collatz:

Si el número es par, dividirlo entre 2.
Si es impar, multiplicarlo por 3 y sumarle 1.
Repetir hasta llegar a 1.
"""
n = int(input("Ingrese un número para la secuencia de Collatz: "))
pasos = 0

while n != 1: # mientras no sea 1 se ejecutan las instrucciones
    if n % 2 == 0:
        n //= 2  # Si es par, dividir entre 2 (//: division entera)
    else:
        n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
    pasos += 1
    print(n, end=" → ")  # Mostrar el proceso

print("\nTotal de pasos:", pasos)



"""
Pedir un número y verificar si es primo usando solo while.
Pistas:
Un número primo es divisible solo por 1 y por sí mismo.
Probar divisiones desde 2 hasta la raíz cuadrada del número.
Si alguna división es exacta, el número no es primo.
"""
n = int(input("Ingrese un número para verificar si es primo: "))

if n < 2:
    print("No es primo")
else:
    divisor = 2
    es_primo = True  # Suponemos que es primo

    while divisor * divisor <= n:
        if n % divisor == 0: # si el resto de la division es cero 
            es_primo = False # es divisible por el divisor, por 
            break # lo que no es primo
        divisor += 1 

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")




"""
Dado un número entero n, generar un triángulo de números 
con el siguiente patrón:
Ejemplo (n = 5):
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15 

Pistas:
Usar while para controlar las filas.
Usar for dentro de while para imprimir los números en cada fila.
Mantener un contador para imprimir el siguiente número en 
la secuencia
"""
n = int(input("Ingrese el número de filas para el triángulo: "))
fila = 1
contador = 1

while fila <= n:
    for i in range(fila):  # Imprimir la cantidad de números en la fila
        print(contador, end=" ")
        contador += 1
    print()  # Nueva línea después de cada fila
    fila += 1
