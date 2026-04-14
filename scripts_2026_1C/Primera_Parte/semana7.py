"""
Automatización de Fechas para Mantenimiento Preventivo En el ámbito de la ingeniería, 
el mantenimiento preventivo es esencial para garantizar la confiabilidad y eficiencia 
de equipos y sistemas. Para evitar fallos inesperados, muchas industrias programan 
inspecciones y mantenimientos en intervalos regulares, como revisiones semanales de 
maquinaria, sistemas eléctricos, motores o sensores industriales. Tu tarea es desarrollar 
un programa que permita registrar múltiples fechas de mantenimiento(se debe ingresar n 
entero y positivo, validar) y determine automáticamente la próxima fecha de inspección, 
sumando 7 días a cada una. 
Ejemplos  | Fechas de Mantenimiento (Día, Mes, Año) |   Fechas Esperadas (+7 días) 
1         | n=1 15,3,2024                           | 22 de marzo de 2024

2         | n=2 31,12,2024 25,12,2024               | 7 de enero de 2025 
                                                      1 de enero de 2025

3         | n=3 31,8,2024 24,9,2024 26,6,2024       | 7 de septiembre de 2024 
                                                      1 de octubre de 2024 
                                                      3 de julio de 2024

Observaciones importantes:
● Se puede suponer que usuario solo cargará números enteros, se recomienda 
usar .split(“,”)(esto no es obligatorio). No se permite usar la libreria datetime. 
● La solución debe ser lo suficientemente general para resolver cualquier entrada 
diferente a las propuestas en los ejemplos. 
● Los estudiantes que tengan soluciones similares llevarán 0 %. 
● La evaluación será realizada será realizada manualmente.
"""
### SOLUCION 1
# Validación de N
while True:
  n = int(input("Ingrese cantidad de fechas: "))

  if n > 0:
    break

fechas = []

for i in range(n):
  entrada = input("Ingrese fecha (dia,mes,año): ")
  partes = entrada.split(",")

  dia = int(partes[0])
  mes = int(partes[1])
  año = int(partes[2])

  # dias de cada mes
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_mes = 31

  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_mes = 30

  else:
    dias_mes = 28

  # sumar 7 dias
  dia = dia + 7

  if dia > dias_mes:
    dia = dia - dias_mes
    mes = mes + 1

    if mes > 12:
      mes = 1
      año = año + 1

  print(dia, "de", mes, "de", año)

### SOLUCION 2
# validar N
n = 0

while n <= 0:
  n = int(input("Ingrese cantidad de fechas: "))

for i in range(n):
  entrada = input("Ingrese fecha (dia,mes,año): ")
  partes = entrada.split(",")

  dia = int(partes[0])
  mes = int(partes[1])
  anio = int(partes[2])

  # sumar 7 dias uno por uno
  for k in range(7):
    dia = dia + 1

    # determinar dias del mes
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      dias_mes = 31

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
      dias_mes = 30

    else:
      dias_mes = 28

    # cambio de mes
    if dia > dias_mes:
      dia = 1
      mes = mes + 1

      if mes > 12:
        mes = 1
        anio = anio + 1

  print(dia, "de", mes, "de", anio)







"""
Crear una secuencia ordenada de números naturales desde el 2 hasta un número límite n.
Validar que n sea un número entero, positivo y mayor o igual a 2. Si la diferencia 
entre dos números primos adyacentes es igual a 2, se identifican como una pareja de 
primos gemelos. Estas parejas se almacenarán en un nuevo vector que mostrará únicamente 
los números que cumplan con dicha condición. Imprimir todas las parejas que cumplan la 
condición dentro del rango y la cantidad de parejas que cumplen la condición.

Ejemplo1 :
Primos gemelos entre 2 y 25: 
3 y 5, 5 y 7, 11 y 13, 17 y 19  
Cantidad de Parejas: 4

Ejemplo 2:
Primos gemelos entre 2 y 50 
3 y 5, 5 y 7, 11 y 13, 17 y 19, 29 y 31, 41 y 43
Cantidad de Parejas: 6

Observaciones importantes 
• La solución debe ser lo suficientemente general para resolver cualquier entrada 
diferente a las propuestas en los ejemplos.
• Los estudiantes que tengan soluciones similares llevarán 0 %.
• La evaluación será realizada manualmente.

Criterios de Evaluación y Ponderación 
1. Entrada y validación de datos (30%) 
2. Determinación de primos gemelos (20%) 
3. Contar parejas de primos gemelos (20%)
4. Imprimir la Salida con formato (20%)
5. Organizacion y Estructura del Código (10%)
"""

### SOLUCION 1
# VALIDAR N

n = 0
while n < 2:
  n = int(input("Ingrese n (>=2): "))

# GENERAR NUMEROS PRIMOS
primos = []
for num in range(2, n + 1):
  es_primo = True
  
  for i in range(2, num):
    if num % i == 0:
      es_primo = False

    if es_primo:
      primos.append(num)

# BUSCAR PRIMOS GEMELOS
gemelos = []
for i in range(len(primos) - 1):
  if primos[i+1] - primos[i] == 2:
    gemelos.append((primos[i], primos[i+1]))

# IMPRIMIR RESULTADOS
print("Primos gemelos entre 2 y", n)
for par in gemelos:
  print(par[0], "y", par[1], end=", ")

print()
print("Cantidad de Parejas:", len(gemelos))




### SOLUCION 2
# VALIDAR N
n = 0
while n < 2:
  n = int(input("Ingrese n (>=2): "))

# BUSCAR PRIMOS GEMELOS
gemelos = []
for num in range(2, n + 1):
  # verificar si num es primo
  primo1 = True

  for i in range(2, num):
    if num % i == 0:
      primo1 = False

  # verificar si num+2 es primo
  if num + 2 <= n:
    primo2 = True

    for j in range(2, num + 2):
      if (num + 2) % j == 0:
        primo2 = False

    if primo1 and primo2:
      gemelos.append((num, num+2))

# IMPRIMIR RESULTADOS
print("Primos gemelos entre 2 y", n)
for par in gemelos:
  print(par[0], "y", par[1], end=", ")

print()
print("Cantidad de Parejas:", len(gemelos))






"""
Para este ejercicio nos interesa calcular el valor del coseno de un ángulo mediante 
el método de aproximación del desarrollo de Taylor. La aproximación está dada por la 
siguiente fórmula: 
cos(x) ≈ Σ_{i=0}^{N} (-1)^i * x^(2*i) / (2*i)!
donde N es la cantidad de términos a ser considerados en la 
aproximación. Ejemplo de aplicación del desarrollo de Taylor Llamaremos alpha al ángulo 
(en grados sexagesimales) y N a la cantidad de términos. Considerando alpha=60 y 
N=4: 
... 
Donde x es el valor de alpha, pero en radianes. Así, se tiene que x=1.04719. 
Es importante resaltar que el programa debe encargarse de realizar la conversión de 
sexagesimales a radianes (sabiendo que pi= 3,14159265359 equivale a 180°). También es 
importante recordar que el símbolo ! representa el factorial de un número (por ejemplo: 
4 != 1*2*3*4). Debe escribir un programa en Python que lea por teclado dos elementos: el 
valor del ángulo (en grados sexagesimales) y un valor N. Se debe validar que el valor del 
ángulo esté en el intervalo [0,360). Además, se debe validar que N sea un número entero 
mayor que 5 y menor que 20. El programa deberá mostrar una tabla con los resultados 
obtenidos por esta fórmula de aproximación, considerando los diferentes valores de N 
que van desde 1 hasta N (inclusive). Como ejemplo del formato, se muestra la salida del 
programa para alpha=60 y N=10: 
ingrese alpha: 60
ingrese N: 10
resultado | N 
0.4516 | 1 
0.5017 | 2 
.... 

El criterio de corrección será el siguiente: 
• Validación del ángulo alpha: 10% 
• Validación de N: 10% 
• Conversión del ángulo a radianes: 10% 
• Cálculo de la aproximación del coseno para un determinado número de términos: 50% 
• Cálculo de la aproximación del coseno para los diferentes nter, según el enunciado: 10% 
• Formato de la tabla de resultados: 10% • Si el programa tiene errores de sintaxis, 
se analiza el proceso; y por cada error de sintaxis se penalizará (-5%)
"""

### SOLUCION 1
# VALIDACION DEL ANGULO

alpha = -1
while alpha < 0 or alpha >= 360:
  alpha = float(input("Ingrese alpha (0 <= alpha < 360): "))

# VALIDACION DE N
N = 0
while N <= 5 or N >= 20:
  N = int(input("Ingrese N (5 < N < 20): "))

# CONVERSION A RADIANES
pi = 3.14159265359
x = alpha * pi / 180

print("resultado | N")

# CALCULO DE APROXIMACION
for nter in range(1, N+1):
  suma = 0

  for k in range(nter):
    # calcular potencia
    potencia = x ** (2*k)

    # calcular factorial
    factorial = 1

    for i in range(1, 2*k + 1):
      factorial = factorial * i

    termino = potencia / factorial
    if k % 2 == 1:
      termino = -termino

    suma = suma + termino

  print(round(suma,4), "|", nter)





### SOLUCION 2
# VALIDACION DEL ANGULO
alpha = -1
while alpha < 0 or alpha >= 360:
  alpha = float(input("Ingrese alpha (0 <= alpha < 360): "))

# VALIDACION DE N
N = 0
while N <= 5 or N >= 20:
  N = int(input("Ingrese N (5 < N < 20): "))

# CONVERSION A RADIANES
pi = 3.14159265359
x = alpha * pi / 180

print("resultado | N")

# APROXIMACION DE TAYLOR
suma = 1
termino = 1
for k in range(1, N+1):
  termino = termino * (-1) * x * x / ((2*k-1)*(2*k))
  suma = suma + termino
  print(round(suma,4), "|", k)