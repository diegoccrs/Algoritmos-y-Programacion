lista = [1,2,3]

tupla = (1,2,3)

diccionario = {"primero": 1, "segundo":[1,2,3]}

x = diccionario["primero"]
y = lista[0]
z = tupla[0]

w = diccionario["segundo"][1] # = 2

print(x)

lista = [1,2,3,4]
for i in lista:
    print(i)

diccionario = {"a1": 15616, "a2": "Caja"}

for i,j in diccionario.items():
    print(f"i = {i}, j = {j}")

for i in diccionario.keys():
    print(f"keys = {i}")

for i in diccionario.values():
    print(f"values = {i}")

diccionario["a1"] = "nuevo valor"
for i in diccionario.values():
    print(f"values = {i}")

diccionario["nueva_key"] = "nueva value"