menu = {"Cachito": 4.00, "Empanada": 3.00, "Pasatelito": 3.50, "Sandwich": 2.50, "Pan tradicional (1 barra)": 1.00, "Pan especial (1 barra)": 1.75, "Café": 1.25, "Jugo": 2.00, "Agua": 0.75, "Dulces (por kilo)": 6.00, "Galletas (por kilo)": 5.75, "Torta": 10.25}




def datos(clientes):
    """
    Función que toma los datos del cliente.

    Argumentos => diccionario de clientes.

    Retorna => diccionario con nombre, cédula y factura actualizados.
    """

    # se pide nombre y se comprueba que sea un ingreso válido
    nombre = input("Ingrese el nombre del cliente: ")
    while not ("".join(nombre.split(" "))).isalpha():
        nombre = input("Ingreso inválido, ingrese el nombre del cliente: ")


    # se pide cédula y se comprueba que sea un ingreso válido
    cedula = input("Ingrese el número de cédula del cliente: ")
    while (not cedula.isnumeric()) or (int(cedula) < 1):
        cedula = input("Ingreso inválido, ingrese el número de cédula del cliente: ")

    # la factura se genera automáticamente, es igual al número de la persona en la base de datos. La factura No.1 le corresponde a la primera persona, la 2 a la segunda y así
    factura = len(clientes["Nombre"]) + 1

    # se guarda la info en el diccionario en su respectiva lista
    clientes["Nombre"].append(nombre.title())
    clientes["Cédula"].append(int(cedula))
    clientes["Factura"].append(factura)

    # se retorna el diccionario con el cliente nuevo
    return clientes



def pedido(clientes):
    """
    Función para tomar el pedido del cliente actual.

    Argumentos => clientes: diccionario de clientes.

    Retorna => diccionario con items y total actualizados.

    """

    # variables para almacenar la información de los items a comprar (tupla con nombre del producto, cantidad a comprar, precio de la unidad, precio total) y el precio total de la compra
    compra = []
    total = 0

    # se muestran todos los productos que se ofrecen numerados
    print("PRODUCTOS\n")
    for i,producto in enumerate(menu):
        print(f"{i+1}. {producto}: ${menu[producto]}")
    print("\n")

    # se usa un while loop para agregar productos a la compra hasta que se decida parar
    while True:
        # se solicita el número correspondiente al producto a comprar
        prod_n = input("Ingrese el número correspondiente al producto a comprar: ")
        while (not prod_n.isnumeric()) or (int(prod_n) < 1):
            prod_n = input("Ingrese un valor válido: ")

        # se solicitan las unidades a adquirir
        amnt = input("Ingrese la cantidad a comprar: ")
        while (not amnt.isnumeric()) or (int(amnt) < 1):
            amnt = input("Ingrese un valor válido: ")
        
        # según el número ingresado anteriormente para seleccionar el producto, se busca en el diccionario y se guarda su nombre y precio en dos variables
        for i,producto in enumerate(menu):
            if i == (int(prod_n) - 1):
                prod = producto
                total_prod = menu[producto] * int(amnt)

        # se agrega a la lista 'compra' una tupla con nombre del producto, cantidad a comprar, precio de la unidad, precio total
        compra.append((prod,amnt,menu[prod],total_prod))

        # se le suma el precio del producto con el que se está trabajando a la variable que guarda el costo total de la compra
        total += total_prod

        print("\n")

        # se ejecuta la función 'mostrar_compra()' para mostrar qué se ha agregado a la factura por ahora
        mostrar_compra(total,compra)

        print("\n")

        # se pregunta si se quiere agregar otra cosa a la compra
        seleccion = input("¿Desea agregar otro producto? ('S' para 'sí', 'N' para 'no'): ")
        while (seleccion.upper() != "S") and (seleccion.upper() != "N"):
            seleccion = input("Ingreso inválido, ¿desea agregar otro producto? ('S' para 'sí', 'N' para 'no'): ")

        print("\n")

        if seleccion.upper() == "S":
            # si la respuesta es afirmativa, se continúa en el while loop
            continue
        else:
            # si no se quiere comprar nada más, se agregan los datos de la compra al diccionario de clientes
            clientes["Items"].append(compra)
            clientes["Total"].append(total)
            return clientes



def mostrar_factura(clientes,index):
    """
    Función que muestra la factura final del cliente actual.

    Argumentos => clientes: diccionario de clientes.

    Retorna => factura con toda la información del cliente impresa.
    """

    print("\t  FACTURA")
    print("--------------------")
    print(f"Nombre: {clientes['Nombre'][index]}")
    print(f"Cédula: {clientes['Cédula'][index]}")
    print(f"Factura #{clientes['Factura'][index]}")
    print("--------------------")
    mostrar_compra(clientes['Total'][index],clientes['Items'][index])
    print("--------------------")
    print(f"Descuento: {clientes['Descuento'][index]}")
    print(f"TOTAL CON DESCUENTO: ${clientes['Total con descuento'][index]}")



def mostrar_compra(total,compra):
    """
    Función para mostrar los productos que se están comprando.

    Argumentos =>
    \n\ttotal: cantidad a pagar por los productos a comprar
    \tcompra: lista de tuplas con la información de cada producto

    Retorna => Nombre, cantidad y precio de los productos que se están adquiriendo.
    """

    for i,item in enumerate(compra):
        print(f"- {item[0]}: {item[1]} X ${item[2]}")
    print("--------------------")
    print(f"\tTOTAL: ${total}")



def mostrar_diccionario(clientes):
    """
    Función que ejecuta la función 'mostrar_factura()' sobre todas las personas registradas en el diccionario de clientes.

    Argumentos => clientes: diccionario de clientes

    Retorna => factura impresa para todos los clientes.

    """

    for i in range(len(clientes["Nombre"])):
        mostrar_factura(clientes,i)
        print("\n"*2)



def descuentos(clientes):
    """
    Función que aplica el descuento que corresponda al cliente.

    Argumentos => clientes: diccionario de clientes

    Retorna => diccionario con descuentos y precio con descuento actualizados.

    """

    # se verifica qué descuento se debe aplicar y se guardan los datos del descuento en su respectivo lugar en el diccionario

    if (clientes["Total"][-1] % 3 == 0) and (clientes["Total"][-1] % 7 == 0):
        clientes["Descuento"].append("15%")
        (clientes["Total con descuento"]).append(clientes["Total"][-1] - (clientes["Total"][-1] * 0.15))


    elif clientes["Total"][-1] % 3 == 0:
        clientes["Descuento"].append("10%")
        (clientes["Total con descuento"]).append(clientes["Total"][-1] - (clientes["Total"][-1] * 0.10))


    elif clientes["Total"][-1] % 7 == 0:
        clientes["Descuento"].append("12%")
        (clientes["Total con descuento"]).append(clientes["Total"][-1] - (clientes["Total"][-1] * 0.12))


    # se retorna el diccionario actualizado
    return clientes



def main():
    clientes = {"Nombre":[], "Cédula": [], "Factura": [], "Items": [], "Total": [], "Descuento": [], "Total con descuento": []}

    while True:

        print("\n1. Nueva factura\n2. Ver facturas")
        eleccion = input("Ingrese el número correspondiente a lo que desea hacer: ")
        while eleccion != "1" and eleccion != "2":
            eleccion = input("Ingrese un valor válido: ")

        if eleccion == "1":
            print("\n")
            datos(clientes)
            print("\n")
            pedido(clientes)
            print("\n")

            if (clientes["Total"][-1] % 3 == 0) or (clientes["Total"][-1] % 7 == 0):
                descuentos(clientes)
                mostrar_factura(clientes,(-1))
                print("\n")
            else:
                clientes["Descuento"].append("0%")
                clientes["Total con descuento"].append(clientes["Total"][-1])
                mostrar_factura(clientes,(-1))
                print("\n")

        else:
            print("\n")
            if len(clientes['Nombre']) < 1:
                print("Todavía no hay compras registradas.")
            else:
                mostrar_diccionario(clientes)
            print("\n")


        seleccion = input("¿Desea realizar alguna otra operación? ('S' para 'sí', 'N' para 'no'): ")
        while (seleccion.upper() != "S") and (seleccion.upper() != "N"):
            seleccion = input("Ingreso inválido, ¿desea realizar alguna otra operación? ('S' para 'sí', 'N' para 'no'): ")

        if seleccion.upper() == "S":
            continue
        else:
            break

main()