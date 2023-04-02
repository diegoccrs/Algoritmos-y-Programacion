# CONTADOR DE LETRAS
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
# muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Introduzca una frase: ")
letter = input("Introduzca una letra: ")

contador = 0
for i in phrase:
    if i == letter:
        contador += 1


print(f"La letra {letter} se repite {contador} veces en la frase")