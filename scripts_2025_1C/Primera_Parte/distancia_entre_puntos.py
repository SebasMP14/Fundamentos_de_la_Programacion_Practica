"""
    Solicite al usuario que ingrese dos puntos, luego imprima en 
    pantalla la distancia entre ellos y el punto medio.
"""
import math
print(math.pi)





x1 = float(input('X1: '))
y1 = float(input('Y1: '))
x2 = float(input('X2: '))
y2 = float(input('Y2: '))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
xm = (x1 + x2)/2 
ym = (y1 + y2)/2

print(f'La distancia entre es: {distancia} \nEl punto medio es ({xm},{ym}')
print("La distancia entre es: ", distancia, "\tEl punto medio es", xm, ", ", ym)

