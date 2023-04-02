#Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable.
#Y pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

key = "contraseña"

password = input("Ingrese la contraseña: ")

while password != key:
    print("La contraseña es incorrecta, intente de nuevo.")
    password = input("Ingrese la contraseña: ")      
print("La contraseña es correcta")   