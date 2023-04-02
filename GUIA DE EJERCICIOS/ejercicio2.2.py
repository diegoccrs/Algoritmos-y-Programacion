# 2.2 PALINDROMO 
# Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha. 
# Por ejemplo: 101 es un número palíndromo, y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.
# Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.

word = input("Ingrese una palabra: ")
reversed_word = word [::-1]

if word == reversed_word:
    print("Es palindromo")
else:
    print("No es palindromo")