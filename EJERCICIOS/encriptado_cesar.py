"""
Introducir una palabra y moverse n espacios a la derecha.
n siendo un numero ingresado por el usuario 
"""

texto = input("Introduce algo: ").lower()
desplazamiento = int(input("Cuantos espacios te quieres mover: "))

abc = "abcdefghijklmnñopqrstuvwxyz"

texto_cifrado = ""

for i in texto:
    if i in abc:
        texto_cifrado += abc[(abc.index(i)+desplazamiento)]
        
print(f"Texto cifrado: {texto_cifrado}")