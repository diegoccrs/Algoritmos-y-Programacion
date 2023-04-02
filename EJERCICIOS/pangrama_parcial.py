"""Verificar que la frase dada es un pangrama y contar la cantidad de letras que se repiten dentro de la frase"""

frase = ("El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo").lower()

def verificacion_pangrama(frase):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for letra in letras:
        if letra not in frase:
            return "No es Pangrama"
    return "Es Pangrama"

print(frase)
print(" ")
print(verificacion_pangrama(frase))
print("\n")

def contador_de_letras(frase):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    contador = []
    for letra in letras:
        if letra in frase:
            contador.append(frase.count(letra))
        else:
            contador.append(0)
    for letra in range(0,len(contador)):
        print(f"{letras[letra]} = {contador[letra]}")

print("Letras repetidas:\n")
print(contador_de_letras(frase))