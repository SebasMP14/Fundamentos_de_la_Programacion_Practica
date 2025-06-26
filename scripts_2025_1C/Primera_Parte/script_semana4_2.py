"""
Pedir al usuario una cadena y mostrarla invertida.
Usar el concepto de secuencias y slicing ([::-1]).
"""
cadena = input("Ingrese una cadena: ")
print(cadena)
invertida = cadena[::-1]
print("Cadena invertida:", invertida)


"""
Crear un diccionario con tres elementos y mostrar solo sus
 valores usando .values().
"""
persona = {"nombre": "Sebas", "edad": 26, "ciudad": "Asunción"}
lista_persona = list(persona.values())
print("Valores del diccionario:", lista_persona)


"""
Pedir al usuario cinco números y almacenarlos en una lista.
Usar sum() para obtener la suma total.
"""
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(5)]
print("Suma de los números:", sum(numeros))

"""
Definir una tupla con los días de la semana y 
recorrerla con un for.
"""
dias = ("L", "M", "X", "J", "V", "S", "D")
for dia in dias:
    print(dia)

print(dia)


"""
Usar for y range para generar la lista de los 
primeros 10 múltiplos de 3
"""
multiplos_de_3 = [3 * i for i in range(1, 11)]
print("Primeros 10 múltiplos de 3:", multiplos_de_3)

lista3 = []
for i in range(1, 11):
    lista3.append(i * 3)
print(lista3)
