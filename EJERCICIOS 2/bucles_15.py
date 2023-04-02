# Escriba un programa que le pregunte al usuario algo y lo ejecute infinitamente hasta que el usuario ingrese "salir".

while True:
    something = input("Introduzca algo: ")
    print(something)
    if something == "salir":
        break  