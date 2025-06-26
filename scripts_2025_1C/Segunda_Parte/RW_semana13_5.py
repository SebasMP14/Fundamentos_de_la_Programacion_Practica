import csv

# Datos a escribir
datos = [
  ['Producto', 'Cantidad', 'Precio'],
  ['Lapiz', 120, 0.5],
  ['Cuaderno', 80, 2.5],
  ['Mochila', 30, 25],
  ['Lapicera', 150, 1.2],
  ['Regla', 100, 1],
  ['Compas', 40, 3.5]
]

# Crear el archivo
with open('ventas.csv', 'w', newline='') as archivo:
  escritor = csv.writer(archivo)
  escritor.writerows(datos)

print("Archivo 'ventas.csv' creado exitosamente.")

###########################################################

import matplotlib.pyplot as plt
# import csv

# Paso 1: Leer el archivo CSV
productos = []
cantidades = []
precios = []

with open('ventas.csv', 'r', newline='') as archivo:
  lector = csv.reader(archivo)
  next(lector)  # Saltar la cabecera
  
  for fila in lector:
    producto, cantidad, precio = fila # "string", 10, 10.1
    productos.append(producto)
    cantidades.append(int(cantidad))
    precios.append(float(precio))

print('Productos:', productos)
print('Cantidades:', cantidades)
print('Precios:', precios)

# Paso 2: Calcular el total de dinero por producto
totales = []

for i in range(len(cantidades)):
  cantidad = cantidades[i]
  precio = precios[i]
  totales.append(cantidad * precio)

print('Totales:', totales)

# Paso 3: Encontrar el producto con mayor recaudación
indice_max = totales.index(max(totales))

# Paso 4: Dibujar el gráfico de barras
colores = ['skyblue'] * len(productos)
colores[indice_max] = 'orange'  # Color especial para el producto top

plt.figure(figsize=(10, 6))
plt.bar(productos, totales, color=colores, edgecolor='black')

# Personalización
plt.title('Recaudación por Producto')
plt.xlabel('Producto')
plt.ylabel('Total Recaudado ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar etiquetas de valor encima de cada barra
for i, total in enumerate(totales):
  plt.text(i, total + 5, f"${total:.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()
