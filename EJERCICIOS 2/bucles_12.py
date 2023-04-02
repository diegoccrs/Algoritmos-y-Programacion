#Escribir un programa que pida al usuario un número entero positivo mayor que 2 
#Y muestre por pantalla si es un número primo o no.

n = int(input("Ingrese un numero entero positivo mayor que 2: "))

i = 2

while n % i != 0:
    i += 1
if i == n:
    print("El numero ", n , " es primo")
else:
    print("El numero ", n ," no es primo")  