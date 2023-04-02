def end_of_the_day(cont_V,cont_B,cont_P,destinos,pasaje,decision,destino_precio,total_V,total_B,total_P):
    print("\n***FINAL DEL DIA***\n")
    print("Numero total de clientes rumbo a Valencia: ",cont_V)
    print("Numero total de clientes rumbo a Barquisimeto: ",cont_B)
    print("Numero total de clientes rumbo a Puerto La Cruz: ",cont_P)
    total_descuento(decision,destinos,pasaje)
    monto_total_neto_expresos_saman(total_V,total_B,total_P,decision,pasaje,destino_precio)

def monto_total_neto_expresos_saman(total_V,total_B,total_P,decision,pasaje,destino_precio):
    if decision == "V":
        if pasaje >= 1 and pasaje <= 10:
            total_V += (descuento(destino_precio,pasaje))+tax(destino_precio,pasaje)
    if decision == "B":
        if pasaje >= 1 and pasaje <= 10:
            total_B += (descuento(destino_precio,pasaje))+tax(destino_precio,pasaje)
    if decision == "P":
        if pasaje >= 1 and pasaje <= 10:
            total_P += (descuento(destino_precio,pasaje))+tax(destino_precio,pasaje)
    print("Monto total neto facturado por expresos Saman: ",total_V+total_B+total_P)

def total_descuento(decision,destinos,pasaje):
    disc = 0
    if decision == "V":
        if pasaje >= 4 and pasaje <=10:
            disc += ((destinos.get("(V)Valencia"))*pasaje)*0.20
    if decision == "B":
        if pasaje >= 4 and pasaje <=10:
            disc += ((destinos.get("(B)Barquisimeto"))*pasaje)*0.20
    if decision == "P":
        if pasaje >= 4 and pasaje <=10:
            disc += ((destinos.get("(P)Puerto La Cruz"))*pasaje)*0.20
    print("Monto total de descuentos otorgados: ",disc)

def tax(destino_precio,pasaje):
    total = destino_precio*pasaje
    tax = total*0.16
    return tax

def descuento(destino_precio,pasaje):
    if pasaje >= 4 and pasaje <= 10:
        total = destino_precio*pasaje
        discount = total - total*0.20
    elif pasaje >= 1 and pasaje <= 3:
        total = destino_precio*pasaje
        discount = total
    return discount

def mostrar_factura(id,pasaje,destino_precio,decision):
    print("\n***FACTURA***")
    print("------------------")
    print("Cedula: ",id)
    print("Cantidad de pasajeros: ",pasaje)
    print("Codigo de Destino: ",decision)
    print("------------------")
    print("Monto bruto: ",destino_precio*pasaje)
    print("Monto con descuento: ",descuento(destino_precio,pasaje))
    print("Impuesto IVA: ",tax(destino_precio,pasaje))
    print("------------------")
    print("Monto neto a pagar: ",(descuento(destino_precio,pasaje))+tax(destino_precio,pasaje),"Bs")
    
def main():
    destinos = {"(V)Valencia": 500, "(P)Puerto La Cruz": 700, "(B)Barquisimeto": 800}
    cont_V = 0
    cont_B = 0
    cont_P = 0
    total_V = 0
    total_B = 0
    total_P = 0
    while True:
        print("***BIENVENIDO A EXPRESOS SAMAN***\n")
        print("1.Comprar pasaje\n2.Salir\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("Destinos disponibles: \n")
            for key,value in destinos.items():
                print(key,":",value,"Bs")
            decision = input("¿A que destino desea dirigirse? ")
            if decision == "V":
                cont_V += 1
                destino_precio = destinos.get("(V)Valencia")
                pasaje = int(input("¿Cuantos pasajes desea comprar? "))
                id = int(input("Perfecto\nPor favor indiquenos su numero de cedula: "))
                mostrar_factura(id,pasaje,destino_precio,decision)
            elif decision == "P":
                cont_P += 1
                destino_precio = destinos.get("(P)Puerto La Cruz")
                pasaje = int(input("¿Cuantos pasajes desea comprar? "))
                id = int(input("Perfecto\nPor favor indiquenos su numero de cedula: "))
                mostrar_factura(id,pasaje,destino_precio,decision)
            elif decision == "B":
                cont_B += 1
                destino_precio = destinos.get("(B)Barquisimeto")
                pasaje = int(input("¿Cuantos pasajes desea comprar? "))
                id = int(input("Perfecto\nPor favor indiquenos su numero de cedula: "))
                mostrar_factura(id,pasaje,destino_precio,decision)
            else:
                print("Ingreso invalido, asegurese de ingresar las letras en mayuscula")
        elif opcion == 2:
            end_of_the_day(cont_V,cont_B,cont_P,destinos,pasaje,decision,destino_precio,total_V,total_B,total_P)
            print("\n")
            print("***GRACIAS POR VISITAR EXPRESOS SAMAN***")
            break
        else:
            print("Ingreso invalido, intente de nuevo")
main()
