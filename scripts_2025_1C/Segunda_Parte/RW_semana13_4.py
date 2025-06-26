"""
Leer un archivo calificaciones.txt con notas de 
estudiantes (0-100).
Agrupar en intervalos de 10 (0-9, 10-19, ..., 90-100) 
y graficar un histograma.
"""
import random

with open('calificaciones.txt', 'a') as archivo:
  for _ in range(100):
    archivo.write(f"{random.randint(0, 100)}\n")

# Leer y agrupar
# for i in range(0, 101, 10):
#   intervalos = {f'{i}-{i+9}': 0}
intervalos = {f'{i}-{i+9}': 0 for i in range(0, 101, 10)}
intervalos['90-100'] = 0  # ajustar el último intervalo

with open('calificaciones.txt', 'r') as archivo:
  for linea in archivo:
    nota = int(linea.strip()) # validar si es necesario
    print(nota)
    if nota == 100:
      intervalos['90-100'] += 1
    else:
      key = f'{(nota//10)*10}-{(nota//10)*10 + 9}'
      print(key)
      intervalos[key] += 1

print(intervalos)

# Graficar
import matplotlib.pyplot as plt

etiquetas = list(intervalos.keys())
frecuencias = list(intervalos.values())

plt.bar(etiquetas, frecuencias, color='brown', edgecolor='black')
plt.title('Distribución de Calificaciones')
plt.xlabel('Rango de notas')
plt.ylabel('Cantidad de estudiantes')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
