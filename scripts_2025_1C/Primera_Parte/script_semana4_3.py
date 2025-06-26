colores = ("rojo", "verde", "azul", "amarillo")
print("Primer color:", colores[0])
print("Último color:", colores[-1])


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Lista concatenada:", lista_concatenada)


nombres = ["Ana", "Luis", "Pedro", "Juan", "Sofía"]
sublista = nombres[:3]
print("Sublista:", sublista)


persona = {"nombre": "Sebas", "edad": 26, "lqsea": "otra variable de cualquier tipo"}
print(persona)
persona["profesión"] = "Ingeniero Mecatrónico"
print(persona)
del persona["edad"]
print("Diccionario actualizado:", persona)


estudiante = {"nombre": "Marta", "carrera": "Informática", "año": 2}
existe = "carrera" in estudiante
print("¿La clave 'carrera' está en el diccionario?", existe)


############################ diferencia entre listas y tuplas
# Se pueden modificar después de ser creadas (agregar, eliminar o cambiar elementos).
# Se definen con corchetes [].
# Son más flexibles, pero un poco más lentas que las tuplas.
lista = [1, "string", 3]
lista_vacia = []
lista.append(4)  # Se puede agregar elementos
lista[0] = 10    # Se puede modificar
print(lista)  # [10, 2, 3, 4]

def imprimirLista(lista):
    for valor_de_lista in lista:
        # print(lista[valor_de_lista])
        print(valor_de_lista)

imprimirLista(lista)

# Tuplas (tuple)
# No se pueden modificar después de ser creadas.
# Se definen con paréntesis ().
# Son más rápidas y usan menos memoria que las listas.
tupla = (1, "string", 3)
# tupla[0] = 10  # Esto daría error porque las tuplas no se pueden modificar
print(tupla)  # (1, 2, 3)



for i in tupla:
    print(i)

lista = list(range(0, 5, 2))
print(lista)

for i in range(5, 0, -2):
    print(i)

lista = list(range(0, 5))
print(lista)
new_list = lista[0:5:2]
print(new_list)
a = lista[3]
print(a)
