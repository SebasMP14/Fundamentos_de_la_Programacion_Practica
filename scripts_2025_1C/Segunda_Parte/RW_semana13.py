# Crear y escribir en un archivo
with open('datos.txt', 'a') as archivo:
  archivo.write('10\n') # tabulación: '\t'
  archivo.write('20\n')
  archivo.write('30\n')
  archivo.write('40\n')
  archivo.write('50\n')

################################################################

# Leer datos del archivo
numeros = []

with open('datos.txt', 'r') as archivo:
  for linea in archivo:
    numero = int(linea.strip())
    numeros.append(numero)

print(numeros)

# ################################################################

# Crear un histograma
frecuencias = {}

for numero in numeros:
  if numero in frecuencias:
    frecuencias[numero] += 1
  else:
    frecuencias[numero] = 1

print(frecuencias)  # {10: 1, 20: 1, 30: 1, 40: 1, 50: 1}

# ################################################################

import matplotlib.pyplot as plt

# Datos
valores = list(frecuencias.keys())
conteos = list(frecuencias.values())

# Crear el gráfico
plt.bar(valores, conteos)

# Personalizar
plt.title('Histograma de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostrar
plt.show()
