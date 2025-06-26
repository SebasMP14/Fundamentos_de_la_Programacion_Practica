"""
Pedir al usuario una cadena y contar cuántas vocales tiene.
Usar un for para recorrer la cadena.
Usar una variable bandera para detectar si hay al menos una vocal.
"""
cadena = input("Ingrese una cadena: ").lower()
print(cadena)
vocales = "aeiouó"
contador = 0
tiene_vocal = False

for letra in cadena:
    print(letra)
    if letra in vocales:
        contador += 1
        tiene_vocal = True

print(f"La cadena tiene {contador} vocales.")
if tiene_vocal:
    print("Se encontraron vocales en la cadena.")
else:
    print("No hay vocales en la cadena.")
