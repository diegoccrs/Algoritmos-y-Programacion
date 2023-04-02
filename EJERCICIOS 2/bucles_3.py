# Partiendo de una frase imprimir palabra por palabra y un contador de palabras totales.

phrase = input("Introduzca una frase: ")

w = ""   #acumulador de elementos

c = 0    #contador de palabras

for i in range(len(phrase)):
    if phrase[i] == " ":
        c = c + 1
        print(w)
        w = ""
    else:
        w = w + phrase[i]
print(w)


print("La frase tiene", c+1 ,"palabras.")  