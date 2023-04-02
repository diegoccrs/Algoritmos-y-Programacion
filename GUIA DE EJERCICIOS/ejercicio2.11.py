# 2.11 PARIDAD
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n = int(input("Introduzca un numero entero: "))

if n%2 == 0:
    print("El numero ", n ," es par")
else:
    print("El numero ", n ," es impar")