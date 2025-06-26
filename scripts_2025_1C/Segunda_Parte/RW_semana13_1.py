import matplotlib.pyplot as plt

# Paso 1: Leer archivo
numeros = []
with open('datos.txt', 'r') as archivo:
    for linea in archivo:
        numeros.append(int(linea.strip()))

# Paso 2: Crear histograma
frecuencias = {}
for numero in numeros:
    frecuencias[numero] = frecuencias.get(numero, 0) + 1
print(frecuencias)

# Paso 3: Visualizar
valores = list(frecuencias.keys())
conteos = list(frecuencias.values())

plt.bar(valores, conteos, color='skyblue', edgecolor='black')
plt.title('Histograma de Datos desde Archivo')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
