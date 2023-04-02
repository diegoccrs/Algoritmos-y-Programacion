# Escriba un programa que le pida al usuario una palabra y le muestre por pantalla el numero de vocales 
# Se deben mostrar la cuenta de las 5 vocales

word = input("Introduzca una palabra: ").lower()

a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

print(f"La palabra {word} tiene {a} veces la letra (a)")
print(f"La palabra {word} tiene {e} veces la letra (e)")
print(f"La palabra {word} tiene {i} veces la letra (i)")
print(f"La palabra {word} tiene {o} veces la letra (o)")
print(f"La palabra {word} tiene {u} veces la letra (u)") 