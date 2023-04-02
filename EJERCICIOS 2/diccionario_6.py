# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

person_data = {}

continuar = True

while continuar:
    key = input("¿Que dato desea introducir? ")
    value = input(key + ": ")
    person_data[key] = value
    print(person_data)
    continuar = input("¿Quieres añadir mas informacion? (Si/No)? ") == "Si" or "si"