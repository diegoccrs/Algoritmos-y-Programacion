# 3.18 PALABRAS
# Realice un algoritmo que dada una palabra ingresada por el usuario calcule cuántas
# letras tiene, cuántas consonantes tiene, cuántas vocales tiene y el número de veces en
# que cada vocal se repite durante la palabra.

word = input("Ingrese una palabra: ").lower()

print()

while not word.isalpha():
    word = input("No puede introducir valores numericos. Intente de nuevo: ").lower()

print(f"{word} tiene {len(word)} letras.")

a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

print()
print(f"{word} tiene {(len(word))-(a+e+i+o+u)} consonantes")
print()
print(f"{word} tiene {a+e+i+o+u} vocales.")
print()
print(f"La a se repite {a} veces")
print(f"La e se repite {e} veces")
print(f"La i se repite {i} veces")
print(f"La o se repite {o} veces")
print(f"La u se repite {u} veces")