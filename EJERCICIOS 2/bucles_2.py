# Calcular el factorial de un número.

n = int(input("Introduzca un numero: "))

x = n
y = n-1

while y != 1:
    x = x*y
    y -= 1

print(f"El factorial de {n} es {x}")     