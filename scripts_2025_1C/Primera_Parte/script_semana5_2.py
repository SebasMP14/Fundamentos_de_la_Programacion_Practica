"""
Un número perfecto es aquel cuya suma de sus 
divisores propios (excluyendo el número) es igual al mismo número.

Ejemplo:
6 → Sus divisores propios son 1, 2, 3 → 1 + 2 + 3 = 6 (Es perfecto)
28 → Sus divisores propios son 1, 2, 4, 7, 14 → 1 + 2 + 4 + 7 + 14 = 28
Pistas:
Recorrer los números desde 1 hasta n//2 para encontrar divisores.
Usar while para sumar los divisores y verificar la condición.
"""
n = int(input("Ingrese un número para verificar si es perfecto: "))
suma_divisores = 0
divisor = 1

while divisor <= n // 2:  # Solo es necesario revisar hasta la mitad del número
    if n % divisor == 0:
        suma_divisores += divisor
    divisor += 1

if suma_divisores == n:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")



"""
Un número es palíndromo si se lee igual de izquierda a derecha 
y de derecha a izquierda.

Ejemplo:
121 →  (Es palíndromo)
123 →  (No es palíndromo)
Pistas:
Invertir el número usando un while (como en el ejercicio anterior).
Comparar el número original con su versión invertida.
"""
n = int(input("Ingrese un número para verificar si es palíndromo: "))
original = n
invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

if original == invertido:
    print("Es un número palíndromo")
else:
    print("No es un número palíndromo")


"""
Convertir un número decimal a binario dividiendo repetidamente por 2 y almacenando los residuos.
Entrada 13
13 / 2 → residuo = 1  
6 / 2 → residuo = 0  
3 / 2 → residuo = 1  
1 / 2 → residuo = 1  
Salida: 1101
Pistas:
Usar while para extraer los residuos con n % 2.
Almacenar los residuos en orden inverso para obtener el binario.
"""
n = int(input("Ingrese un número decimal para convertir a binario: "))
binario = ""

while n > 0:
    residuo = n % 2
    binario = str(residuo) + binario  # Agregar el residuo al inicio
    n //= 2

print("Binario:", binario)


"""
Dado un número n, encontrar el primer número en la serie de Fibonacci que sea mayor a n.

Ejemplo:
Entrada: 20
Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
Salida: 21

Pistas:
Usar while para generar la serie de Fibonacci hasta superar n.
"""
n = int(input("Ingrese un número para encontrar el primer Fibonacci mayor: "))
a, b = 0, 1

while b <= n:
    a, b = b, a + b  # Generar el siguiente número de Fibonacci

print("El primer número de Fibonacci mayor que", n, "es:", b)



"""
Dado un número n, generar un patrón donde cada fila contiene números en orden inverso:

Ejemplo (n = 5):

5 4 3 2 1  
4 3 2 1  
3 2 1  
2 1  
1  
Pistas:
Usar while para controlar las filas.
Usar for dentro de while para imprimir los números en orden inverso.
"""
n = int(input("Ingrese un número para el patrón: "))
fila = n

while fila > 0:
    for num in range(fila, 0, -1):  # Imprimir números en orden inverso
        print(num, end=" ")
    print()  # Salto de línea después de cada fila
    fila -= 1
