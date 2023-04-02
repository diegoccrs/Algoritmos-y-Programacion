# ECO
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
# usuario escriba “salir” que terminará el programa.

while True:
    word = input("Ingrese algo: ")
    if word == "salir":
        break
    print(word)