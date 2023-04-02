# 3.4 SUCESION DE FIBONACCI 
# La sucesión de Fibonacci se calcula en base a la siguiente fórmula:
# f (x) = 0 si x = 0
# f (x) = 1 si x = 1
# f (x) = f (x-1) + f (x-2) si x > 1
# Escribe un programa que, dado un número n, imprima la sucesión de Fibonacci, separada por comas, hasta el número igual o más cercano que haya por debajo de n.

# Ejemplos de output:
# Si n = 8:
# 0,1,1,2,3,5,8
# Si n = 15:
# 0,1,1,2,3,5,8,13


n = input("Ingrese un número positivo entero, este será el límite de la sucesión: ")
while not n.isnumeric() or int(n)<1:
    n = input("Ingreso inválido, intente de nuevo: ")

x = 0
y = 1
z = 1

sucesion = []
sucesion.append(str(x))

while z <= int(n):
    sucesion.append(str(z))
    z = x+y
    x = y
    y = z

print(",".join(sucesion))