from cliente import Cliente
from bebidas import BebidaAlcoholica,BebidaNoAlcoholica

def ver_estadisticas(cont_ba,cont_bna,total_clientes,compras_totales_a,compras_totales_na):
    print("***ESTADISTICAS SAMAN BAR****\n")
    print(f"Cantidad total de bebidas alcoholicas vendidas: {cont_ba}")
    print(f"Cantidad total de bebidas no alcoholicas vendidas: {cont_bna}")
    print(f"Cantidad de clientes que han comprado: {total_clientes}")
    if total_clientes == 0:
        print("Promedio total de compra: ",0)
    else:
        print(f"Promedio total de compra: {(compras_totales_a+compras_totales_na)/total_clientes}")

def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num-1)+fib(num-2)

def monto_total(compra_a,compra_na,edad):
    monto_t = compra_a + compra_na
    if monto_t > 1:
        cont = 0
        for i in range(2,monto_t):
            resto = monto_t%i
            if resto == 0:
                cont += 1
        if cont == 0:
            discount = monto_t*0.10
            monto_primo = monto_t-discount
            print("Se le ha otorgado un 10% de descuento")
            print("-"*30)
            print(f"Descuento primo: {discount}$")
            print(f"Monto con descuento primo: {monto_primo}$")
        else:
            monto_primo = monto_t
            print("No se ha otorgado el descuento primo :(")
            print(f"Monto sin descuento primo: {monto_primo}$")

    monto_fibo = monto_primo-(monto_primo*0.05)
    lista = []
    for x in range(edad):
        y = fib(x)
        lista.append(y)
    if edad not in lista:
        print("-"*30)
        print(f"No hay descuento fibo")
        monto_fibo = monto_primo
    else:
        print("-"*30)
        print(f"Se le ha otorgado un 5% de descuento")
        print("-"*30)
        print(f"Descuento Fibo: {monto_primo*0.05}$")
        print(f"Monto con descuento fibo: {monto_fibo}$")
    
    print("-"*30)
    print(f"Monto total a pagar: {monto_fibo}$")

def mostrar_factura(nombre,edad,id,bebidas_cliente,compra_a,compra_na,cont_a,cont_na):
    cliente_registrado = Cliente(nombre,edad,id)
    print("***FACTURA***")
    print("-"*30)
    print("DATOS DEL CLIENTE")
    cliente_registrado.mostrar()
    print("-"*30)
    print("BEBIDAS COMPRADAS")
    for i,j in enumerate(bebidas_cliente):
        print(i+1)
        j.mostrar()
        print()
    print(f"Cantidad de bebidas compradas: {cont_a+cont_na}")
    print("-"*30)
    monto_total(compra_a,compra_na,edad)

def registrar_bebidas(ba,bna):
    print()
    print("1- Bebida Alcoholica\n2- Bebida No Alcoholica")
    tipo = int(input("Ingrese que tipo de bebida desea registrar: "))
    if tipo == 1:
        nombre = input("Ingrese nombre de la bebida: ").capitalize()
        precio = int(input("Ingrese el precio ($) que tendra esta bebida: "))
        grado = int(input("Ingrese los grados de alcohol de la bebida: "))
        print()
        print("Bebida registrada con exito")
        bebida_registrada = BebidaAlcoholica(nombre,precio,grado)
        ba.append(bebida_registrada)
    elif tipo == 2:
        nombre = input("Ingrese nombre de la bebida: ")
        precio = int(input("Ingrese el precio ($) que tendra esta bebida: "))
        temperatura = int(input("Ingrese la temperatura de la bebida: "))
        print()
        print("Bebida registrada con exito")
        bebida_registrada = BebidaNoAlcoholica(nombre,precio,temperatura)
        bna.append(bebida_registrada)
    else:
        print("Error, porfavor ingrese datos validos")

def main():
    ba = [BebidaAlcoholica("Cerveza",2,30),BebidaAlcoholica("Mojito",3,45)]
    bna = [BebidaNoAlcoholica("Agua Mineral",1,6),BebidaNoAlcoholica("Pepsi",2,7)]
    bebidas_cliente = []
    cont_ba = 0     
    cont_bna = 0    
    compra_a = 0    
    compra_na = 0   
    cont_a = 0
    cont_na = 0 
    total_clientes = 0 
    compras_totales_a = 0
    compras_totales_na = 0
    print("***BIENVENIDO A SAMAN BAR***")
    print()
    while True:
        print("1- Registrar bebidas\n2- Ver Bebidas Disponibles y Comprar\n3- Estadisticas\n4- Salir\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            registrar_bebidas(ba,bna)
        elif opcion == 2:
            print("Antes de ver las bebidas disponibles, el cliente debe ingresar sus datos")
            nombre = input("Ingrese su nombre: ").capitalize()
            edad = int(input("Ingrese su edad: "))
            id = int(input("Ingrese su numero de cedula: "))
            print()
            while True:
                if edad <= 18:
                    print("2.Bebidas No Alcoholicas\n")
                else:
                    print("1- Bebidas Alcoholicas\n2.Bebidas No Alcoholicas\n")
                eleccion = int(input("Ingrese el tipo de bebida que desea: "))
                if eleccion == 1:
                    for i,j in enumerate(ba):
                        print("-"*15,i+1,"-"*15)
                        j.mostrar()
                    compra = int(input("Ingrese el numero de la bebida deseada: "))
                    cantidad = int(input("Ingrese cuantas desea: "))
                    b_cliente = ba[compra-1]
                    compra_a += (b_cliente.precio)*cantidad
                    bebidas_cliente.append(b_cliente)
                    cont_ba += cantidad
                    cont_a += cantidad
                    compras_totales_a += (b_cliente.precio)*cantidad
                elif eleccion == 2:
                    for i,j in enumerate(bna):
                        print("-"*15,i+1,"-"*15)
                        j.mostrar()
                    compra = int(input("Ingrese el numero de la bebida deseada: "))
                    cantidad = int(input("Ingrese cuantas desea: "))
                    b_cliente = bna[compra-1]
                    compra_na += (b_cliente.precio)*cantidad
                    bebidas_cliente.append(b_cliente)
                    cont_bna += cantidad
                    cont_na += cantidad
                    compras_totales_na += (b_cliente.precio)*cantidad
                else:
                    print("Error, vuelva a intentar")
                
                otro = input("\n¿Desea comprar otra bebida? ('S' para 'si', 'N' para 'no'):  ")
                while otro.upper() != 'S' and otro.upper() != 'N':
                    otro = input("Por favor ingrese un valor valido: ")
                if otro.upper() == "S":
                    continue
                else:
                    mostrar_factura(nombre,edad,id,bebidas_cliente,compra_a,compra_na,cont_a,cont_na)
                    total_clientes += 1
                    cont_a = 0
                    cont_na = 0 
                    compra_a = 0
                    compra_na = 0
                    bebidas_cliente.clear()
                    break
        elif opcion == 3:
            ver_estadisticas(cont_ba,cont_bna,total_clientes,compras_totales_a,compras_totales_na)
        elif opcion == 4:
            break
        else:
            print("Error, porfavor ingrese datos validos")

main()