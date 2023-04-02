"""
Se dice que un número es feliz cuando cumple que si sumamos los cuadrados de sus dígitos 
y seguimos el proceso con los resultados de esas sumas que vamos obteniendo en cada paso, el resultado final, 
cuando llegamos a una suma con un solo dígito, es 1.

Ejemplo: 
7**2 = 49
4**2 + 9**2 = 97
9**2 + 7**2 = 130
1**2 + 3**2 + 0**2 = 10
1**2 + 0**2 = 1

El numero 7 es feliz
"""

def numero_feliz(numero):
    x = numero
    suma_cuadrados = []
    while True:
        if x == 1:
            return True
        
        x = sum(int(z)**2 for z in str(x))
        if x in suma_cuadrados:
            return False
        
        suma_cuadrados.append(x)

numero_a_verificar = input("Ingresa un numero: ")

if numero_feliz(numero_a_verificar):
    print(f"{numero_a_verificar} es numero feliz")
else:
    print(f"{numero_a_verificar} no es numero feliz")