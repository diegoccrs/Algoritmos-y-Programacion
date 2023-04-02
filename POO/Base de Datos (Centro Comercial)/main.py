# 9.2 MALL DATABASE 
# Un centro comercial te ha contratado para que diseñes un programa que los ayude a almacenar de una 
# manera más sencilla toda la información de sus tiendas. 
# Cada tienda tiene nombre, tipo de tienda, piso en el que está (hay PB, 1, 2 y 3), RIF, 
# nombre del propietario y teléfono del propietario.
# Luego de almacenar esto en su base de datos, debe existir una función que permita 
# ver la información organizada de cada local del centro comercial.
# Como requerimientos adicionales pidieron:
# Al mostrar todas las tiendas registradas, deben aparecer ordenadas por nombre, piso o tipo, según se solicite.

#tipos = ["Women's Apparel", "Men's Apparel", "Children's Apparel", "Footwear", "Health & Beauty", "Jewelry & Watches", "Sporting Goods & Apparel", "Luggage & Handbags", "Optical/Eyewear","Electronics","Food", "Entertainment & Attractions", "Toys & Hobbies", "Home Décor", "Department Store", "Services", "Other"]

from tienda import Tienda 

tipos = ["Women's Apparel", "Men's Apparel", "Children's Apparel", "Footwear", "Health & Beauty", "Jewelry & Watches", "Sporting Goods & Apparel", "Luggage & Handbags", "Optical/Eyewear","Electronics","Food", "Entertainment & Attractions", "Toys & Hobbies", "Home Décor", "Department Store", "Services", "Other"]

def registrar_tienda(tiendas):
    nombre = input("Ingrese el nombre de la tienda: ")
    print("\n")
    for valor,t in enumerate(tipos):
        print(f"{valor+1}. {t}")

    tipo = input("Introduzca el numero correspondiente al tipo de tienda que esta registrando: ")
    while not tipo.isnumeric() or int(tipo) not in range(len(tipos)):
        tipo = input("Porfavor ingrese un valor valido: ")

    for valor,t in enumerate(tipos):
        if tipo == str(valor+1):
            tipo = t
    
    print("\n0. PB\n1. P1\n2. P2\n3. P3")
    piso = input("Ingrese el numero correspondiente al piso en que se encuentra la tienda: ")
    while not piso.isnumeric() or int(piso) not in range(0,4):
        piso = input("Por favor ingrese un valor valido: ")

    if int(piso) == 0:
        piso = "PB"

    rif = input("\nIngrese numero de RIF de la tienda: ").upper()

    propietario = input("\nIngrese nombre del propietario: ").title()

    telefono = input("\nIngrese el numero de telefono del propietario (sin espacios y sin caracteres especiales): ")
    while not telefono.isnumeric() or len(telefono) != 11:
        telefono = input("Por favor ingrese valores validos: ")

    nueva_tienda = Tienda(nombre,tipo,piso,rif,propietario,telefono)
    tiendas.append(nueva_tienda)

    print("\nNueva tienda registrada con exito")
    nueva_tienda.mostrar()

    return tiendas

def ver_tiendas(tiendas,seleccion):
    if int(seleccion) == 2:
        tiendas.sort(key = lambda tienda: tienda.nombre.capitalize())
    elif int(seleccion) == 3:
        tiendas.sort(key = lambda tienda: tienda.piso)
    else:
        tiendas.sort(key = lambda tienda: tienda.tipo)
    
    for valor,t in enumerate(tiendas):
        print("---",valor+1,"-----------")
        t.mostrar()

def main():
    tiendas = []
    print("***Bienvenido a la base de datos del centro comercial***")
    while True:
        print("\n1. Registrar Tienda\n2. Ver tiendas registradas por nombre\n3. Ver tiendas registradas por piso\n4. Ver tiendas registradas por tipo\n")
        seleccion = input("Ingrese una opcion: ")
        while not seleccion.isnumeric() or int(seleccion) not in range(1,5):
            seleccion = input("Por favor ingrese un valor valido: ")
        print("\n")
        if int(seleccion) == 1:
            registrar_tienda(tiendas)
        else:
            if len(tiendas) == 0:
                print("Todavia no hay tiendas registradas")
            else:
                ver_tiendas(tiendas,seleccion)

        otro = input("\n¿Desea relizar alguna otra operacion? ('S' para 'si', 'N' para 'no'):  ")
        while otro.upper() != 'S' and otro.upper() != 'N':
            otro = input("Por favor ingrese un valor valido: ")
        if otro.upper() == "S":
            continue
        else:
            break

main()