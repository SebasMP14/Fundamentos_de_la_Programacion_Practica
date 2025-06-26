"""
 Sistema de Control de Temperatura en un Invernadero
Contexto: Un invernadero inteligente ajusta la ventilación 
según el promedio de temperaturas medidas por sensores.

Objetivo:
Crear una función que reciba una lista de temperaturas y 
devuelva su promedio.

Según el promedio, activar una recomendación:

Si el promedio es mayor a 30°C → “Activar ventiladores”

Si es menor a 15°C → “Activar calefacción”

Si está entre 15°C y 30°C → “Temperatura ideal.”
"""
# from Repaso_semana11 import promedio as prom
import Repaso_semana11 as rep11


def recomendacion(lista):
    prome = rep11.promedio(lista)

    if prome > 30:
        return "Activar Ventiladores"
    elif prome < 15:
        return "Activar calefaccion"
    else:
        return "Temperatura ideal"

lista = [10, 11, 10.5, 13, 14, 14.6]
print(recomendacion(lista))



















def promedio(lista): # del ejercicio anterior
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def control_temperatura(lecturas):
    prom = promedio(lecturas)
    if prom > 30:
        return "¡Activar ventiladores!"
    elif prom < 15:
        return "¡Activar calefacción!"
    else:
        return "Temperatura ideal."

# Ejemplo
temperaturas = [28, 32, 35, 30]
print(control_temperatura(temperaturas))
