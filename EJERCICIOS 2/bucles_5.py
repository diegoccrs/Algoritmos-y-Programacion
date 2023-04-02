#Escribir un programa que pregunte al usuario su edad 
#Y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))

for i in range(age):
    print("Has cumplido ", i+1 , " años") 