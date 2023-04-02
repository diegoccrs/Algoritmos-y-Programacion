# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> 
# y su número de teléfono es <teléfono>.

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
d = input("Ingrese su direccion: ")
number = int(input("Ingrese su numero de telefono: "))

data = {"Nombre":name, "Edad":age, "Direccion":d,"Telefono":number}

print("\n")

print(f"{name} tiene {age} años, vive en {d} y su numero de telefono es {number}")