"""
Análisis de Seguridad de Contraseñas
Contexto: Una app revisa contraseñas ingresadas por los usuarios y debe evaluarlas.

Objetivo:
Escribir una función recursiva que cuente cuántas mayúsculas hay en una contraseña.

Escribir otra función que determine si la contraseña es segura, si cumple:

Al menos 8 caracteres
Al menos 1 mayúscula
Al menos 1 dígito
"""





































def contar_mayusculas(cadena):
    if cadena == "":
        return 0
    elif cadena[0].isupper():
        return 1 + contar_mayusculas(cadena[1:])
    else:
        return contar_mayusculas(cadena[1:])

def contiene_digito(cadena):
    for c in cadena:
        if c.isdigit():
            return True
    return False

def es_segura(clave):
    return len(clave) >= 8 and contar_mayusculas(clave) >= 1 and contiene_digito(clave)

print(es_segura("clave123"))       # False
print(es_segura("Clave123"))       # True
