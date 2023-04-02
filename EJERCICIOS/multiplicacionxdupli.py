"""Multiplicacion por duplicacion"""

numero = int(input("Ingrese un numero: "))
multiplicador = int(input("Ingrese por cuanto se va a multiplicar el numero: "))
cont = 0
while numero >= 1:
    if numero%2 !=0:
        cont = cont + multiplicador
    numero = numero//2
    multiplicador = multiplicador * 2
print(f"La respuesta es: {cont}")