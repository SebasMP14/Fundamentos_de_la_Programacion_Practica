### Estructuras condicionales, operadores lógicos y relacionales
# antes Entrada → Proceso → Salida
# ahora Entrada → Decisión → Proceso → Salida
"""
entrada
si edad >= 18
    permitir acceso
si no
    denegar acceso
salida
"""

#################### Operadores relacionales
# >	    mayor que
# <	    menor que
# >=	mayor o igual
# <=	menor o igual
# ==	igual
# !=	distinto

# print(5 > 3)
# print(type(3 < 2))
# print(5 >= 3)
# print(5 == 4)





"""
if condicion:
    instruccion
    # con indentacion (se hace presionando la tecla "tab")
# sin indentacion
"""

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad")
# else:
#     print("Menor de edad")







"""
if condicion:
    instruccion
else:
    instruccion
"""

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Mayor de edad")
# else:
#     print("Menor de edad")






# ### else if → elif
# nota = int(input("Ingrese nota: "))

# if nota >= 90:
#     print("Excelente")
# elif nota >= 70:
#     print("Aprobado")
# else:
#     print("Reprobado")


print( (5 < 3) and (5 < 3))



#################### Operadores Lógicos
# | Operador | Significado |
# | -------- | ----------- |
# | and      | y           |
# | or       | o           |
# | not      | no          |

# edad = int(input("Edad: "))
# tiene_entrada = input("Tiene entrada (si/no): ")

# if edad >= 18 and tiene_entrada == "si":
#     print("Puede entrar")
# else:
#     print("No puede entrar")




# dia = input("Dia: ")

# if dia == "sabado" or dia == "domingo":
#     print("Fin de semana")
#     pass





# llueve = False

# if not llueve:
#     print("Salir")





""" Solicitar al user 3 numeros e imprimir el mayor """
# a = float(input("ingrese el primer numero: "))
# b = float(input("ingrese el segundo numero: "))
# c = float(input("ingrese el tercer numero: "))

# if a > b and a > c:
#     print("El mayor es a: ", a)
# elif b > a and b > c:
#     print("b: ", b)
# elif a == b: 
#     print("a y b son iguales...")
# else:
#     print("El mayor es c: ", c)




"""
Un estudiante aprueba si:

nota ≥ 60

Mostrar:

"Aprobado" o "Reprobado"
"""



"""
Escriba un algoritmo que solicite: día, mes, año
Determine si la fecha es válida.
Considere:
- mes entre 1 y 12
- día entre 1 y 31
- febrero tiene máximo 28 días
- abril, junio, septiembre, noviembre tienen 30 días
"""
# dia = int(input("día: "))

# if dia <= 31 and dia >= 1:
#     mes = int(input("mes: "))
#     if mes <= 12 and mes >= 1:
#         año = int(input("año: "))
#         if año <= 2026 and año >= 1:
#             if mes == 2 and dia > 28:
#                 print("dia incorrecto para febrero")
#             elif mes == 2 and dia <= 28:
#                 print("dia para febrero correcto")
#             else:
#                 if mes == 4 or mes == 6 or mes == 9 or mes == 11:
#                     if dia > 30:
#                         print("dia incorrecto")
#                     else:
#                         print("mes y dia correctos")
#                 else:
#                     print("mes, dia y año correctos: ", dia, "/", mes, "/", año)
#                     print(f"{mes}/{dia}/{año} correctos")
#             # elif mes == 4 and dia > 30:
#             #     print("dia para abril incorrecto")
#             # elif mes == 
#         else:
#             print("año incorrecto.")
#     else: 
#         print("mes incorrecto.")
# else: 
#     print("dia incorrecto.")






"""
Un trabajador cobra 10.000 Gs por hora normal, horas superiores 
a 8 se pagan al doble.

Solicitar:
- nombre
- horas trabajadas

Calcular y mostrar sueldo total por día.
"""
nombre = input("ingrese el nombre del trabajador: ")
horas = int(input("ingrese las hs trabajadas en el dia: "))

if horas <= 8:
    print("Se le debe pagar a ", nombre, ": ", horas * 10000, "Gs.")
else:
    aux = horas - 8
    salario = (8 * 10000) + (aux * 10000 * 2)
    print("El salario de ", nombre,  "es: ", salario, " Gs.")


"""
Solicitar dos números e imprimirlos en orden ascendente.
"""


"""
Solicitar un año y determinar si es bisiesto.

Reglas:
Un año es bisiesto si es divisible por 4 y no por 100
o es divisible por 400
"""

