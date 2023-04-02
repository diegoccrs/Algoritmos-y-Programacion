# 2.7 CALCULO DE AREAS
# Se requiere un sistema para calcular el área de figuras geométricas sencillas
# Donde el usuario ingresará en qué figura está interesado. 
# El sistema debe permitir la solicitud de circunferencias, elipses, cuadrados, rectángulos, triángulos y rombos; 
# Solicitando para cada uno la información necesaria. Si existe información que sea constante, deben manejarla como tal.

pi = 3.14159265359

print("Figuras: \n\t1-Circulo\n\t2-Triangulo\n\t3-Cuadrado\n\t4-Elipse\n\t5-Rombo")

operation = int(input("¿Que area desea calcular? "))

if operation == 1:
    radio = float(input("Ingrese el radio del circulo: "))
    print("Area: ",pi*(radio**2))
elif  operation == 2:
    base = float(input("Ingrese una base: "))
    altura = float(input("Ingrese un altura: "))
    print("Area: ",(base*altura)/2)
elif operation == 3:
    base = float(input("Ingrese una base: "))
    altura = float(input("Ingrese un altura: "))
    print("Area: ",base*altura)
elif operation == 4:
    radio_mayor = float(input("Ingrese radio mayor: "))
    radio_menor = float(input("Ingrese radio menor: "))
    print("Area: ",radio_mayor*radio_menor*pi)
elif operation == 5:
    diag_mayor = float(input("Ingrese diagonal mayor: "))
    diag_menor = float(input("Ingrese diagonal menor: "))
    print("Area: ",(diag_mayor*diag_menor)/2)
else:
    print("Error, la opcion no esta disponible")