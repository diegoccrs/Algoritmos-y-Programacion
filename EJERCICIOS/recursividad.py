"""Funcion Recursiva que devuelve la cuenta regresiva de un numero dado"""

def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)

cuenta_atras(10)