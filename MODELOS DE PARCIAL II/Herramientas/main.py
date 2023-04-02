from cliente import * 
from herramientas import *

def ver_estadisticas(num_clientes,cont_p,cont_h,cont_c,cliente_p,cliente_h,cliente_c):
    print(f"Numero de clientes que compraron: {num_clientes}")
    if cliente_p == 0:
        print(f"Promedio de compra en herraminetas de plomeria: ",0)
    else:
        print(f"Promedio de compra en herraminetas de plomeria: {(50*cont_p)/cliente_p}")
    if cliente_h == 0:
        print(f"Promedio de compra en herraminetas de herreria: ",0)
    else:
        print(f"Promedio de compra en herraminetas de herreria: {(40*cont_h)/cliente_h}")
    if cliente_c == 0:
        print(f"Promedio de compra en herraminetas de carpinteria: ",0)
    else:
        print(f"Promedio de compra en herraminetas de carpinteria: {(30*cont_c)/cliente_c}")
    print(f"Total facturado en herramientas de plomeria: {50*cont_p}$")
    print(f"Total facturado en herramientas de herreria: {40*cont_h}$")
    print(f"Total facturado en herramientas de carpinteria: {30*cont_c}$")
    print("\n")

def monto_total(cont2p,cont2h,cont2c):
    monto = (50*cont2p) + (40*cont2h) + (30*cont2c)
    if monto > 1:
        cont = 0
        for i in range(2,monto):
            resto = monto%i
            if resto == 0:
                cont += 1
        if cont == 0:
            discount = monto*0.10
            print("Se le ha otorgado un 10% de descuento")
            print("-"*20)
            print(f"Monto total a pagar: {monto-discount}")
        else:
            print(f"Monto total a pagar: {monto}$")

def mostrar_factura(nuevo_cliente,añadidas,cont2p,cont2h,cont2c):
    print("***FACTURA***")
    print("-"*30)
    nuevo_cliente.mostrar()
    print("-"*30)
    print("Herramientas compradas: \n")
    for i in añadidas:
        print(i.show(),"\n")
    print(f"Cantidad de herramientas de plomeria en total: {cont2p} ")
    print(f"Cantidad de herramientas de herreria en total: {cont2h} ")
    print(f"Cantidad de herramientas de carpinteria en total: {cont2c} ")
    print("-"*30)
    monto_total(cont2p,cont2h,cont2c)

def main():
    herr_plomeria = [Plomeria("Plomerplus","Rojo",50,"Plomeria",5,True,False)]
    herr_herreria = [Herreria("Herreras","Azul",40,"Herreria",20)]
    herr_carpinteria = [Carpinteria("Carpinter","Verde",30,"Carpinteria",2)]
    añadidas = []
    num_clientes = 0
    cliente_p = 0
    cliente_h = 0
    cliente_c = 0
    cont_p = 0
    cont_h = 0
    cont_c = 0
    cont2p = 0
    cont2h = 0
    cont2c = 0
    print("***BIENVENIDO A SAMAN TOOLS***\n")
    while True:
        print("1. Comprar herramientas\n2. Ver estadisticas\n3. Salir\n")
        opcion = int(input("Ingrese una opcion: "))
        print("\n")
        if opcion ==  1:
            while True:
                print("1. Herramientas de Plomeria")
                print("2. Herramientas de Herreria")
                print("3. Herramientas de Carpinteria")
                eleccion = int(input("\nIngrese que tipo de herramienta desea comprar: "))
                print("\n")
                if eleccion == 1:
                    for i,a in enumerate(herr_plomeria):
                        print("-"*15,i+1,"-"*15)
                        a.show()
                        print("\n")
                    compra = int(input("Que desea comprar de este inventario: "))
                    cantidad = int(input("Ingrese cuantas quiere: "))
                    cont_p += cantidad
                    cont2p += cantidad
                    cliente_p += 1
                    if compra == (i+1):
                        añadidas.append(a)
                elif eleccion == 2:
                    for i,a in enumerate(herr_herreria):
                        print("-"*15,i+1,"-"*15)
                        a.show()
                        print("\n")
                    compra = int(input("Que desea comprar de este inventario: "))
                    cantidad = int(input("Ingrese cuantas quiere: "))
                    cont_h += cantidad
                    cont2h += cantidad
                    cliente_h += 1
                    if compra == (i+1):
                        añadidas.append(a)
                else:
                    for i,a in enumerate(herr_carpinteria):
                        print("-"*15,i+1,"-"*15)
                        a.show()
                        print("\n")
                    compra = int(input("Que desea comprar de este inventario: "))
                    cantidad = int(input("Ingrese cuantas quiere: "))
                    cont_c += cantidad
                    cont2c += cantidad
                    cliente_c += 1
                    if compra == (i+1):
                        añadidas.append(a)

                otro = input("\n¿Desea comprar otra herramienta? ('S' para 'si', 'N' para 'no'):  ")
                while otro.upper() != 'S' and otro.upper() != 'N':
                    otro = input("Por favor ingrese un valor valido: ")
                if otro.upper() == "S":
                    continue
                else:
                    print("Herramientas escogidas, porfavor ingrese sus datos a continuacion para facturar\n")
                    nombre = input("Ingrese su nombre: ").capitalize()
                    edad = int(input("Ingrese su edad: "))
                    id = int(input("Ingrese su numero de cedula: "))
                    telefono = int(input("Ingrese  su numero de telefono: "))
                    print("\n")
                    nuevo_cliente = Cliente(nombre,edad,id,telefono)
                    num_clientes += 1
                    print("Cliente registrado con exito")
                    print("\n")
                    mostrar_factura(nuevo_cliente,añadidas,cont2p,cont2h,cont2c)
                    cont2p = 0
                    cont2h = 0
                    cont2c = 0
                    añadidas.clear()
                    break
        elif opcion == 2:
            ver_estadisticas(num_clientes,cont_p,cont_h,cont_c,cliente_p,cliente_h,cliente_c)
        else: 
            break
main()