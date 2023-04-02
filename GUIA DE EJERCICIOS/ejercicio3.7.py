# FACTORIALES 
# Realice un algoritmo que calcule el factorial de un número.

n = int(input("Ingrese un numero para calcular su factorial: "))

f = n
c = n-1

while c != 1:
    f = f*c
    c -= 1

print(f"El factorial de {n} es {f}")