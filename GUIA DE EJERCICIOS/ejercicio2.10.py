# DIVISIONES
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese otro numero: "))

if n2 == 0:
    print("El divisor no puede ser 0")
else:
    print(n1/n2)