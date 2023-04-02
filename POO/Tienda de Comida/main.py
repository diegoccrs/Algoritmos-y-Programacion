# En una tienda de comida tenemos venta de bebidas y de alimentos, donde ambos tienen un nombre, precio 
# y una calificacion del 1 al 5.
# Los alimentos se dividen en postres, plato principal y ensaladas, mientras que las bebidas pueden o no ser alcoholicas, 
# de ser estas podran variar sus grados de alcohol
# Se tiene que un cliente ingresa su nombre,CI, y metodo de pago a la cuenta.
# Lo que se debera hacer es que el usuario elija los alimentos el menu y los cargue en la factura al final, se imprime 
# el nombre de la persona, con todo lo que compro, su metodo de pago, su cedula y la cuenta total. 

from comida import *
from cliente import Cliente

menu_comida = [Alimento("Hamburguesa de queso",2.5,4,"Plato Principal"),Alimento("Pizza Familiar",7,5,"Plato Principal")]
menu_bebida = [Bebida("Agua",0.5,1),Bebida("Coca Cola",1,2),BebidaAlcoholica("Cerveza",1.5,3,"30 grds")]

def ver_menu_de_bebidas(menu_bebida,monto):
    for i,j in enumerate(menu_bebida):
        print("-"*10,i+1,"-"*10)
        j.mostrar()
    eleccion = int(input("Ingrese el numero de lo que desea comprar: "))
    if eleccion == 1:
        monto.append(0.5)
    elif eleccion == 2:
        monto.append(1)
    else:
        monto.append(1.5)
    return monto


def ver_menu_de_comida(menu_comida,monto):
    for i,j in enumerate(menu_comida):
        print("-"*10,i+1,"-"*10)
        j.mostrar()
    eleccion = int(input("Ingrese el numero de lo que desea comprar: "))
    if eleccion == 1:
        monto.append(2.5)
    else:
        monto.append(7)
    return monto

def mostrar_factura(monto):
    nombre = input("Ingrese su nombre: ")
    cedula = int(input("Ingrese  su numero de cedula: "))
    metodo = input("Seleccione un metodo de pago ('Efectivo' o 'Tarjeta'): ")
    usuario = Cliente(nombre,cedula,metodo)
    print("\n")
    total = sum(monto)
    print("FACTURA")
    print("-"*30)
    print("Cliente: ")
    print("\n")
    usuario.mostrar()
    print("-"*30)
    print(f"Monto total a pagar: {total}$")
    print("-"*30)
    print("Gracias por su compra")


def main():
    monto = []
    print("***Bienvenido a nuestro Food Shop***")
    while True:
        print("\n1. Comida\n2. Bebida\n3. Facturar\n4. Salir")
        seleccion = int(input("¿Que desea agregar?\n-->"))
        if seleccion == 1: 
            ver_menu_de_comida(menu_comida,monto)
        elif seleccion == 2:
            ver_menu_de_bebidas(menu_bebida,monto)
        elif seleccion == 3:
            mostrar_factura(monto)
        elif seleccion == 4:
            print("Gracias por su visita")
            break
        else:
            print("Error, vuelva a intentar")

        otro = input("\n¿Desea relizar alguna otra operacion? ('S' para 'si', 'N' para 'no'):  ")
        while otro.upper() != 'S' and otro.upper() != 'N':
            otro = input("Por favor ingrese un valor valido: ")
        if otro.upper() == "S":
            continue
        else:
            break

main()