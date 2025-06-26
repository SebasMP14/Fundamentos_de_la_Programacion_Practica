# Bucles while (mientras)

contador = 1 # declarado antes del bucle
while contador <= 5: # mientras la condicion sea verdadera ejecutar ...
    print(f"Iteración {contador}") # intruccion 1
    contador += 1 # instruccion n, se aumenta el contador

## Comparacion con el ciclo for 
for contador in range(1, 6):
    print(f"Iteración {contador}")

###################################

# ejemplo de aplicación
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ")
    print(f"Escribiste: {respuesta}")

# comparacion con ciclo for
for i in range(10): # se puede limitar la cantidad de intentos
    respuesta = input("Escribe algo (o 'salir' para terminar): ")
    print(f"Escribiste: {respuesta}")
    if respuesta == "salir":
        break # rompe el bucle (tambien funciona con while pero
    # para eso integra un condicional)

"""
Errores comunes:
- Bucles infinitos
- Olvidar actualizar la variable de control (ciclos while)
- Condiciones incorrectas."""

# Calcular el factorial de un nro

n = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    #factorial = factorial * contador
    contador += 1

print(f"El factorial de {n} es {factorial}.")

n = int(input("ingrese el nro"))
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es {factorial}.")



# Imprima la secuencia de fibonacci
n = int(input("Ingrese cuántos números de Fibonacci mostrar: "))
a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1

