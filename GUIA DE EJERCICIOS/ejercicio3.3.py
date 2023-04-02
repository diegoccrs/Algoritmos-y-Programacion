# DADOS
# Con dos dados, al azar, se pueden obtener números entre 2 y 12 de varias formas. 
# Crea un programa que reciba por teclado un número entre 2 y 12 
# Y retorne las combinaciones posibles de números para que su suma sea igual al número ingresado 
# (no debe repetirse la combinación, por ejemplo, 4-5 y 5-4 debe mostrarse solo una vez).

# Ejemplos de output:
# Combinaciones para 5:
# * 1-4
# * 2-3
# Combinaciones para 9:
# * 3-6
# * 4-5

n = input("Ingrese un numero entre 2 y 12: ")

while not n.isnumeric() or int(n) not in range(2,13):
    n = input("Valor invalido, por favor ingrese un valor valido: ")
n = int(n)

combinaciones = []

for x in range(1,7):
    if not sorted([x,(n-x)]) in combinaciones and ((n-x) in range(1,7)):
        combinaciones.append([x,(n-x)])

print(f"Combinaciones para {n}:")
for i,combinacion in enumerate(combinaciones):
    print(f"\t* {combinacion[0]}-{combinacion[1]}")