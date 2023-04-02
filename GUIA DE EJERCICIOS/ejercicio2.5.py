# 2.5 UPPER & LOWER
# Realiza un programa que tome por teclado una palabra y verifique que solo contenga letras.
# Luego, recorriendo el string, cada vez que haya una vocal, debe convertirse a mayúscula. 
# Todas las consonantes deben estar en minúscula.

#Ejemplos de output:
	#hAmbUrgUEsA
	#AprEndEr
	#dIApOsItIvA

word = input("Ingrese una palabra: ").lower()

if not word.isalpha():
    print("ERROR, NO PUEDE INGRESAR NUMEROS")

if "a" in word:
    word = word.replace("a","A")

if "e" in word:
    word = word.replace("e","E")

if "i" in word:
    word = word.replace("i","I")

if "o" in word:
    word = word.replace("o","O")

if "u" in word:
    word = word.replace("u","U")

print(word)