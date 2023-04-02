# Escriba un programa que le pida al usuario un numero entero positivo 
# Y muestre por pantalla su tabla de multiplicar

n = int(input("Ingrese un numero: "))

for i in range(1,11,1):
    print(f"{n} x {i} =",n*i) 