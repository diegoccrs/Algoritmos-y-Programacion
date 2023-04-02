"""Pangrama: Una frase que contiene todas las letras del alfabeto ingles"""

frase = input("Introduzca una frase para verificar si es pangrama o no: ")

def verificacion_pangrama(frase):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in letters:
        if i not in frase.lower():
            return "No es Pangrama"
    return "Es Pangrama"

print(verificacion_pangrama(frase))