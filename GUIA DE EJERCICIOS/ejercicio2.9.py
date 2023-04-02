# 2.9 VERIFICACION DE MAYORIA DE EDAD
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

age = int(input("Ingrese su edad: "))

if age > 18:
    print("Eres mayor de edad")
elif age > 0 and age < 18:
    print("Eres menor de edad")
else:
    print("ERROR, SU EDAD NO PUEDE SER NEGATIVA")