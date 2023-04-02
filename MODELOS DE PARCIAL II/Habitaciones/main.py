from habitaciones import Suite,Doble,Sencilla
from cliente import Cliente

def ver_estadisticas(clientes_alojados,acompañantes_totales_s,acompañantes_totales_d,acompañantes_totales_sen,noches_totales_s,noches_totales_d,noches_totales_sen):
    print(f"Cantidad de clientes alojados: {clientes_alojados}")
    print(f"Promedio de alojamiento por tipo de habitacion: {(acompañantes_totales_d+acompañantes_totales_s+acompañantes_totales_sen)/3}")
    print(f"Total facturado en Suites: {100*acompañantes_totales_s*noches_totales_s}")
    print(f"Total facturado en Dobles: {60*acompañantes_totales_d*noches_totales_d}")
    print(f"Total facturado en Sencillas: {40*acompañantes_totales_sen*noches_totales_sen}")

def monto_total(noches_s,noches_d,noches_sen,acompañantes_s,acompañantes_d,acompañantes_sen,edad):
    monto = (noches_s*100*acompañantes_s) + (noches_d*60*acompañantes_d) + (noches_sen*40*acompañantes_sen)
    contador = 1
    suma = 0
    while contador < monto:
        if monto%contador == 0:
            suma += contador
        contador = contador + 1 
    if suma > monto:
        monto_abundante = monto - (monto*0.10)
        print("Se le ha otorgado un 10% de descuento")
        print(f"Monto total: {monto}")
        print(f"Descuento: {monto*0.10}")
        print("-"*30)
        print(f"Monto total a pagar con descuento: {monto_abundante}")
    else:
        print(f"Monto total a pagar: {monto}")

def mostrar_factura(nuevo_cliente,añadidas,noches_s,noches_d,noches_sen,acompañantes_s,acompañantes_d,acompañantes_sen):
    print("***FACTURA***\n")
    print("-"*30)
    print("Datos del cliente: \n")
    nuevo_cliente.mostrar()
    print("-"*30)
    for m,n in enumerate(añadidas):
        print(m+1,")")
        n.mostrar()
    print("-"*30)
    print(f"Cantidad de noches totales: {noches_s + noches_d + noches_sen}")
    print(f"Cantidad de acompañantes: {acompañantes_s+acompañantes_d+acompañantes_sen}")
    print("-"*30)
    monto_total(noches_s,noches_d,noches_sen,acompañantes_s,acompañantes_d,acompañantes_sen)

def main():
    suites = [Suite(3,3,100,True),Suite(3,4,100,False)]
    dobles = [Doble(2,3,60,"Individual"),Doble(3,4,60,"Matrimonial")]
    sencillas = [Sencilla(2,3,40,True),Sencilla(3,3,40,False)]
    añadidas = []
    noches_s = 0
    noches_d = 0
    noches_sen = 0
    clientes_alojados = 0
    acompañantes_cliente = 0
    acompañantes_totales_s = 0
    acompañantes_totales_d = 0
    acompañantes_totales_sen = 0
    noches_totales_s = 0
    noches_totales_d = 0
    noches_totales_sen = 0
    acompañantes_s = 0
    acompañantes_d = 0
    acompañantes_sen = 0
    print("***BIENVENIDO A SAMAN HOTELS***")
    while True:
        print("1- Habitaciones y Registro de Hospedaje\n2- Ver Estadisticas\n3- Salir")
        opcion = int(input("Ingrese una opcion: "))
        print()
        if opcion == 1:
            while True:
                print("TIPOS DE HABITACIONES DISPONIBLES\n")
                print("1. Suite\n2. Doble\n3. Sencilla\n")
                eleccion = int(input("Ingrese que tipo de habitacion desea: "))
                if eleccion == 1:
                    for i,j in enumerate(suites):
                        print("-"*15,i+1,"-"*15)
                        j.mostrar()
                    decision = int(input("Ingrese el numero de Suite que quiere: "))
                    noches = int(input("Ingrese cuantas noches se va a hospedar: "))
                    acompañantes_s = int(input("Ingrese el numero de personas que se va a hospedar en la habitacion elegida: "))
                    acompañantes_totales_s += acompañantes_s
                    noches_s += noches
                    noches_totales_s += noches_s
                    escogida = suites[decision-1]
                    añadidas.append(escogida)
                    print()
                elif eleccion == 2:
                    for i,j in enumerate(dobles):
                        print("-"*15,i+1,"-"*15)
                        j.mostrar()
                    decision = int(input("Ingrese el numero de habitacion Doble que quiere: "))
                    noches = int(input("Ingrese cuantas noches se va a hospedar: "))
                    acompañantes_d = int(input("Ingrese el numero de personas que se va a hospedar en la habitacion elegida: "))
                    acompañantes_totales_d += acompañantes_d
                    noches_d += noches
                    noches_totales_d += noches_d
                    escogida = suites[decision-1]
                    añadidas.append(escogida)
                    print()
                elif eleccion == 3:
                    for i,j in enumerate(sencillas):
                        print("-"*15,i+1,"-"*15)
                        j.mostrar()
                    decision = int(input("Ingrese el numero de habitacion Sencilla que quiere: "))
                    noches = int(input("Ingrese cuantas noches se va a hospedar: "))
                    acompañantes_sen = int(input("Ingrese el numero de personas que se va a hospedar en la habitacion elegida: "))
                    acompañantes_totales_sen += acompañantes_sen
                    noches_sen += noches
                    noches_totales_sen += noches_sen
                    escogida = suites[decision-1]
                    añadidas.append(escogida)
                    print()
                else:
                    print("Error, porfavor ingrese datos validos")

                otro = input("\n¿Desea comprar otra habitacion? ('S' para 'si', 'N' para 'no'):  ")
                while otro.upper() != 'S' and otro.upper() != 'N':
                    otro = input("Por favor ingrese un valor valido: ")
                if otro.upper() == "S":
                    continue
                else:
                    print("Listo, habitaciones escogidas. Por favor ingrese sus datos a continuacion\n")
                    nombre = input("Ingrese su nombre: ").capitalize()
                    edad = int(input("Ingrese su edad: "))
                    id = int(input("Ingrese su numero de cedula: "))
                    telefono = int(input("Ingrese su numero telfonico: "))
                    print()
                    clientes_alojados += acompañantes_s + acompañantes_d + acompañantes_sen + 1 #este uno es el cliente que esta haciendo la compra de habitaciones
                    acompañantes_cliente = acompañantes_s + acompañantes_d + acompañantes_sen

                    nuevo_cliente = Cliente(nombre,edad,id,telefono,acompañantes_cliente)
                    print("Cliente registrado con exito\n")
                    mostrar_factura(nuevo_cliente,añadidas,noches_s,noches_d,noches_sen,acompañantes_s,acompañantes_d,acompañantes_sen)
                    print("Gracias por su compra")
                    añadidas.clear()
                    acompañantes_s = 0
                    acompañantes_d = 0 
                    acompañantes_sen = 0
                    noches_s = 0
                    noches_d = 0 
                    noches_sen = 0
                    break
        elif opcion == 2:
            ver_estadisticas(clientes_alojados,acompañantes_totales_s,acompañantes_totales_d,acompañantes_totales_sen,noches_totales_s,noches_totales_d,noches_totales_sen)
        elif opcion == 3:
            print("Hasta luego, gracias por visitar Saman Hotels")
            break
        else:
            print("Error, porfavor ingrese valores validos")
    
main()