# 3.17 NÚMEROS PREVIOS
# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas

n = int(input("Ingrese un numero entero positivo: "))

for numbers in range(n,-1,-1):
    print(numbers, end = ",")