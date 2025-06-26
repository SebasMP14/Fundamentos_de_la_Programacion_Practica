from math import pi


a = 6.0
b = 3
print("La suma es: ", a+b)



nombre = input("¿Cuál es tu nombre?")  
print("Hola, " + nombre + "!")
print(pi)



num1 = float(input("Ingrese el primer número: "))  
num2 = float(input("Ingrese el segundo número: "))  
suma = num1 + num2  
print("La suma es:", suma)


# Calcule la media de tres numeros
num1 = int(input("num1"))
num2 = float(input("num2"))
num3 = int(input("num3"))
print("La media de los nros es: ", (num1+num2+num3)/3)
degrees = float(input(""))
print(degrees / 2 / 3.14)



# Calcule el area de un circulo
radio = float(input("ingrese el radio"))
area = 3.14*(radio**2)
print("El area del circulo es: ", area)

# Fahrenheit a grados celsius
far = float(input("Ingrese la temperatura en fahrenheit: "))
print("El quivalente en grados Celsius es: ", (far - 32) * (5/9) )


# Edad en dias



# Comparación de números


entero = int(input("Ingresa un número entero: "))
decimal = float(input("Ingresa un número decimal: "))
texto = input("Ingresa una cadena de texto: ")

print("El tipo de dato de entero es:", type(entero))
print("El tipo de dato de decimal es:", type(decimal))
print("El tipo de dato de texto es:", type(texto))


a = 1.6
print(type(a))
b = round(a)
print(b)

a = '5'
print(a.isdigit())
