"""
Leer edades y crear un histograma de grupos
Leer de un archivo edades.txt una lista de edades.
Agrupar en rangos:
0-17: Menores
18-59: Adultos
60+: Mayores
Luego hacer un gráfico de barras mostrando cuántos hay en cada grupo.
"""

with open('edades.txt', 'a') as archivo:
  archivo.write('15\n22\n72\n55\n38\n16\n72\n55\n38\n13\n80\n')

# Leer y clasificar
menores = adultos = mayores = 0

with open('edades.txt', 'r') as nombre:
  for linea in nombre:
    edad = int(linea.strip())
    if edad <= 17:
      menores += 1
    elif edad <= 59:
      adultos += 1
    else:
      mayores += 1

# Graficar
import matplotlib.pyplot as plt

grupos = ['Menores', 'Adultos', 'Mayores']
cantidades = [menores, adultos, mayores]
print(cantidades)
plt.bar(grupos, cantidades, color=['green', 'blue', 'orange'])
plt.title('Distribución por Edad')
plt.ylabel('Cantidad de personas')
plt.grid(axis='y')
plt.show()
