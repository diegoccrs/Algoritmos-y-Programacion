#Escribir un programa que pida al usuario un número entero
#Y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = int(input("Ingrese un numero entero positivo: "))

for i in range(num):
    for j in range(i+1):
        print("*", end = "")
    print("")    