"""
Comparación visual entre búsqueda lineal y binaria
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Datos base
lista = list(range(1, 200))  # Lista del 1 al 20
objetivo = 144

# Cambiar a 'lineal' o 'binaria'
modo = 'binaria'

# Preparar la figura
fig, ax = plt.subplots()
rects = ax.bar(range(len(lista)), lista, color='skyblue')
titulo = ax.set_title("")

def actualizar_lineal(i):
    for j, bar in enumerate(rects):
        bar.set_color('skyblue')
    if i < len(lista):
        rects[i].set_color('orange')
        if lista[i] == objetivo:
            rects[i].set_color('green')
            titulo.set_text(f"Encontrado en índice {i}")
            ani.event_source.stop()
        else:
            titulo.set_text(f"Probando índice {i}")
    return rects

# Variables para búsqueda binaria
izq = 0
der = len(lista) - 1
pasos_binarios = []

# Preprocesar pasos para binaria
while izq <= der:
    medio = (izq + der) // 2
    pasos_binarios.append((izq, medio, der))
    if lista[medio] == objetivo:
        break
    elif lista[medio] < objetivo:
        izq = medio + 1
    else:
        der = medio - 1

def actualizar_binaria(i):
    if i >= len(pasos_binarios):
        ani.event_source.stop()
        return rects
    for bar in rects:
        bar.set_color('skyblue')
    izq, medio, der = pasos_binarios[i]
    for j in range(izq, der + 1):
        rects[j].set_color('orange')
    rects[medio].set_color('red')
    if lista[medio] == objetivo:
        rects[medio].set_color('green')
        titulo.set_text(f"Encontrado en índice {medio}")
        ani.event_source.stop()
    else:
        titulo.set_text(f"Buscando entre índices {izq} y {der}")
    return rects

# Elegir modo
if modo == 'lineal':
    ani = animation.FuncAnimation(fig, actualizar_lineal, frames=len(lista), interval=700, repeat=False)
    titulo.set_text("Búsqueda Lineal")
else:
    ani = animation.FuncAnimation(fig, actualizar_binaria, frames=len(pasos_binarios), interval=1000, repeat=False)
    titulo.set_text("Búsqueda Binaria")

plt.ylim(0, max(lista)+5)
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.show()
