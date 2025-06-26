num_str = input("Ingrese un nro de 5 cifras: ")
cent_num = num_str[2]
print("El nro es: ", num_str)
print("La centena del nro es: ", cent_num)

cadena = "algoescrito"
a = cadena[0:4:2]
print(a)

for i in range(1,7,2):
    print(str(i))


















try:
    # Solicitar el número (debe ser entre 0 y 9999)
    numero = int(input("Ingresa un número (0-9999): "))

    # Descomponer el número
    mil = numero // 1000
    centena = (numero % 1000) // 100
    decena = (numero % 100) // 10
    unidad = numero % 10

    # Mostrar el resultado
    print(f"Unidades de mil: {mil}")
    print(f"Centenas: {centena}")
    print(f"Decenas: {decena}")
    print(f"Unidades: {unidad}")

    mil = (numero // 1000) * 1000
    centena = ((numero % 1000) // 100) * 100
    decena = (numero % 100) // 10
    unidad = numero % 10

    # Mostrar el resultado
    print(f"Unidades de mil: {mil}")
    print(f"Centenas: {centena}")
    print(f"Decenas: {decena * 10}")
    print(f"Unidades: {unidad}")

except ValueError:
    print("Error: ingrese un número entero")
except : 
    print("Error...")
    