"""
Calcular el área de una figura según el tipo.
    Descripción: Crear una función que reciba
    el tipo de figura ("círculo", "rectángulo" o "triángulo")
    y los datos necesarios para calcular su área.
"""
# area_figura("circulo", 10)
# area_figura("rectangulo", 10, 11)
range(0, 10, 2)
range(10, 2)
range(10)

import math

def area_figura(tipo, base, altura=0):
    if tipo == "círculo":
        return math.pi * base**2
    elif tipo == "rectángulo":
        return base * altura
    elif tipo == "triángulo":
        return (base * altura) / 2
    else:
        return "Tipo no válido"

# Ejemplos
print(area_figura("círculo", 5))           # Área del círculo
print(area_figura("rectángulo", 4, 6))     # Área del rectángulo
print(area_figura("triángulo", 3, 7))      # Área del triángulo



"""
Calcular el promedio de una lista de números: Escribir una 
función que reciba una lista de números y devuelva su promedio.
"""




def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

print(promedio([4, 5, 6, 7]))  # 5.5



"""
Verificar si una palabra contiene solo vocales
    Descripción: Usar recursividad para verificar si todos 
    los caracteres de una palabra son vocales.
"""




def solo_vocales(palabra):
    if palabra == "":
        return True
    elif palabra[0].lower() not in "aeiou":
        return False
    else:
        return solo_vocales(palabra[1:])

print(solo_vocales("aeiou"))   # True
print(solo_vocales("auexi"))   # False
string = "asdfghjkl"
print(string[0])
print(string[2:])
print(string[2:5])
print(string[2:-2])







"""
Sumar los digitos de un nro entero positivo con una 
función recursiva
"""





def suma_digitos(n):
    if n < 10:
        print(n)
        return n
    else:
        print(n)
        return (n % 10) + suma_digitos(n // 10)

# Ejemplo
print(suma_digitos(345))  # 12 (3 + 4 + 5)
