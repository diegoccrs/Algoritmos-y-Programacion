# BUSCADOR DE NOMBRES
# Realice un programa que dado un array de nombres pida al usuario introducir un
# nombre y verificar si este está o no en el array.

names = ["Juan" , "Alberto" , "Ana" ,"Manuela"]

n = input("Ingrese un nombre: ")

if n not in names:
    print("Nombre no es encuentra en la lista")
else:
    print("Si se encuentra en la lista")