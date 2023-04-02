"""Metodo de ordenamiento"""

def ordenamiento_burbuja(lista):
    for n in range(len(lista)-1,0,-1):
        for i in range(n):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


numeros = [7,19,2,13,5,23,29,11,17]
print(numeros)

ordenamiento_burbuja(numeros)
print(numeros)