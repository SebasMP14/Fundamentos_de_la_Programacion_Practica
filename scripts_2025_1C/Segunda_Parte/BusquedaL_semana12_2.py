"""
Buscar el primer nro par
"""
def primer_par(lista):
    for i, numero in enumerate(lista):
        if numero % 2 == 0:
            return i
    return -1

print(primer_par([3, 5, 7, 8, 11]))  



"""
Contar las veces que aparezca un nro natural
"""
def contar_apariciones(lista, objetivo):
    contador = 0
    for numero in lista:
        if numero == objetivo:
            contador += 1
    return contador

print("contar apariciones: ", contar_apariciones([1, 2, 3, 2, 4, 2], 2))  


"""
Buscar una palabra en una lista ordenada
"""
def buscar_palabra(lista, palabra):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == palabra:
            return medio
        elif lista[medio] < palabra:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

palabras = ["avion", "casa", "gato", "perro", "zorro"]
print(buscar_palabra(palabras, "gato"))   
resultado = buscar_palabra(palabras, "zorro")
if ( resultado == -1 ):
    print("variable no encontrada")    
else:
    print(f"El valor está en el indice: {resultado}")


