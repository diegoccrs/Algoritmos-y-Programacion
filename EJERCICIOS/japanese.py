"""PROGRAMA DONDE EL USUARIO INGRESE SU NOMBRE Y LE DEVUELVA EL MISMO NOMBRE EN JAPONES"""

lista = ["ka","tu","mi","te","ku","lu","ji","ri","ki","zu","me","ta","rin","to","mo","no","ke","shi","ari","chi","do","ru","na","mei","fu","ra"]

name = input("Ingrese su nombre: ").lower()
x = ""
for i in name:
    if i == "a":
        x+= lista[0]
    elif i == "b":
        x+= lista[1]
    elif i == "c":
        x+= lista [2]
    elif i == "d":
        x+= lista [3]
    elif i == "e":
        x+= lista [4]
    elif i == "f":
        x+= lista [5]
    elif i == "g":
        x+= lista [6]
    elif i == "h":
        x+= lista [7]
    elif i == "i":
        x+= lista [8]
    elif i == "j":
        x+= lista [9]
    elif i == "k":
        x+= lista [10]
    elif i == "l":
        x+= lista [11]
    elif i == "m":
        x+= lista [12]
    elif i == "n":
        x+= lista [13]
    elif i == "o":
        x+= lista [14]
    elif i == "p":
        x+= lista [15]
    elif i == "q":
        x+= lista [16]
    elif i == "r":
        x+= lista [17]
    elif i == "s":
        x+= lista [18]
    elif i == "t":
        x+= lista [19]
    elif i == "u":
        x+= lista [20]
    elif i == "v":
        x+= lista [21]
    elif i == "w":
        x+= lista [22]
    elif i == "x":
        x+= lista [23]
    elif i == "y":
        x+= lista [24]
    elif i == "z":
        x+= lista [25]
    
print("Nombre en japones:",x)