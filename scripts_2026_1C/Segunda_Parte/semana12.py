# """
# UNIDAD: RECURSIVIDAD

# OBJETIVO DE LA CLASE:
# - Comprender qué es la recursividad
# - Identificar caso base y caso recursivo
# - Comparar con soluciones iterativas
# - Aplicar recursividad a problemas clásicos y de ingeniería
# - Analizar errores comunes (recursión infinita, stack overflow conceptual)
# - Resolver ejercicios sin usar listas complejas ni librerías

# Problema:
# Hay tareas que naturalmente se definen en términos de sí mismas.

# Ejemplo:
# - factorial
# - potencias
# - división repetida
# - estructuras como árboles

# Idea clave:
# Un problema se resuelve resolviendo una versión más pequeña del mismo problema.

# Eso es RECURSIVIDAD.

# Una función recursiva es una función que se llama a sí misma.

# Toda función recursiva debe tener:

# 1) CASO BASE:
#   - condición de parada
#   - evita recursión infinita

# 2) CASO RECURSIVO:
#   - llamada a la misma función con un problema más pequeño
# """

# """ Factorial
# Definición matemática:

# n! = n * (n-1)!

# Caso base:
# 0! = 1
# """
# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)

# print(factorial(5))  # 120

# # Version iterativa
# def factorial_iter(n):
#   resultado = 1
#   for i in range(1, n+1):
#     resultado = resultado * i
#   return resultado

# print(factorial_iter(5))



# """ Potencia
# x^n = x * x^(n-1)
# """
# def potencia(x, n):
#   if n == 0:
#     return 1
#   else:
#     return x * potencia(x, n-1)

# print(potencia(2, 5))  # 32



# """ Suma de dígitos
# Ejemplo:
# 1234 = 4 + suma(123)
# """
# def suma_digitos(n):
#   if n == 0:
#     return 0
#   else:
#     return n % 10 + suma_digitos(n // 10)

# print(suma_digitos(1234))  # 10



# """
# def funcion(problema):
#   if caso_base:
#     return solucion_simple
#   else:
#     return combinar(problema, funcion(problema_mas_pequeño))
# """






# """
# ENUNCIADO:
# Determinar si un número es capicúa (palíndromo)
# SIN usar strings.

# Idea:
# Comparar primer y último dígito.
# """

# def invertir(n, inv=0):
#   if n == 0:
#     return inv
#   else:
#     return invertir(n // 10, inv*10 + n % 10)

# def es_capicua(n):
#   return n == invertir(n)

# print(es_capicua(12321))





# """
# ENUNCIADO:
# Convertir un número entero positivo a binario
# usando recursividad.

# Salida como número (no string).
# """

# def binario(n):
#   if n < 2:
#     return n
#   else:
#     return binario(n // 2) * 10 + (n % 2)

# print(binario(10))





# def es_primo_rec(n, i=2):
#   if n < 2:
#     return False

#   if i * i > n:
#     return True

#   if n % i == 0:
#     return False

#   return es_primo_rec(n, i+1)

# print(es_primo_rec(17))  # True










# """
# ENUNCIADO:

# Un número se dice "ESPECIAL" si cumple TODAS las siguientes condiciones:

# 1) La suma de sus divisores propios (excluyendo el número)
#   es igual a otro número dentro del rango analizado (2 a N).

# 2) La cantidad de divisores del número es PAR.

# 3) La suma de sus dígitos es un número PERFECTO.

# -----------------------------------------------------

# Recordatorios:

# Número PERFECTO:
# Es un número cuya suma de divisores propios es igual al mismo número.
# Ejemplo:
# 6 -> 1 + 2 + 3 = 6

# -----------------------------------------------------

# El programa debe:

# 1) Leer un número N (validar: entero positivo > 1)
# 2) Analizar todos los números desde 2 hasta N
# 3) Determinar cuáles son "ESPECIALES"
# 4) Mostrar:
#   - cada número especial
#   - cuántos hay en total

# -----------------------------------------------------

# RESTRICCIONES:

# - NO usar strings
# - NO usar listas
# - Implementar funciones:
#   - versión ITERATIVA
#   - versión RECURSIVA
# """

# ==========================================================
# FUNCIONES ITERATIVAS
# ==========================================================

def suma_divisores(n):
  suma = 0

  for i in range(1, n):
    if n % i == 0:
      suma += i

  return suma


def cantidad_divisores(n):
  contador = 0

  for i in range(1, n+1):
    if n % i == 0:
      contador += 1

  return contador


def suma_digitos(n):
  suma = 0

  while n > 0:
    suma += n % 10
    n = n // 10

  return suma


def es_perfecto(n):
  return suma_divisores(n) == n


def es_especial_iter(n, N):
  suma = suma_divisores(n)

  cond1 = suma >= 2 and suma <= N   # o simplemente: suma <= N (ya que suma >=1 siempre)
  cond2 = cantidad_divisores(n) % 2 == 0
  cond3 = es_perfecto(suma_digitos(n))

  return cond1 and cond2 and cond3


# # ==========================================================
# # FUNCIONES RECURSIVAS
# # ==========================================================

def suma_divisores_rec(n, i=1):
  if i == n:
    return 0

  if n % i == 0:
    return i + suma_divisores_rec(n, i+1)
  else:
    return suma_divisores_rec(n, i+1)


def cantidad_divisores_rec(n, i=1):
  if i > n:
    return 0

  if n % i == 0:
    return 1 + cantidad_divisores_rec(n, i+1)
  else:
    return cantidad_divisores_rec(n, i+1)


def suma_digitos_rec(n):
  if n == 0:
    return 0
  return n % 10 + suma_digitos_rec(n // 10)


def es_perfecto_rec(n):
  return suma_divisores_rec(n) == n


def es_especial_rec(n, N):
  suma = suma_divisores(n)

  cond1 = suma >= 2 and suma <= N   # o simplemente: suma <= N (ya que suma >=1 siempre)
  cond2 = cantidad_divisores(n) % 2 == 0
  cond3 = es_perfecto(suma_digitos(n))

  return cond1 and cond2 and cond3




# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

# validación
N = 0

while N <= 1:
  N = int(input("Ingrese N (>1): "))


print("=== VERSION ITERATIVA ===")

contador_iter = 0

for num in range(2, N+1):
  if es_especial_iter(num):
    print("Especial:", num)
    contador_iter += 1

print("Cantidad (iterativa):", contador_iter)


print("\n=== VERSION RECURSIVA ===")

contador_rec = 0

for num in range(2, N+1):
  if es_especial_rec(num):
    print("Especial:", num)
    contador_rec += 1

print("Cantidad (recursiva):", contador_rec)