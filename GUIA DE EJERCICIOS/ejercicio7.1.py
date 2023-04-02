# 7.1 FAST FOOD CHAIN
# Una cadena de comida rápida te necesita para la creación de un programa con el que se pueda llevar 
# una base de datos de los productos que ofrecen en su menú con su precio. 
# Para ello, deberás aplicar lo que has aprendido sobre las diferentes estructuras de datos de Python.
# Este negocio ofrece hamburguesas, nuggets, papas fritas, helados y bebidas.
# Las hamburguesas pueden ser: clásica ($4.00), doble carne ($4.80), BBQ ($4.40) y de pollo ($4.20),.
# Los nuggets pueden ser: de 15 piezas ($6.20) o de 30 piezas ($10.50).
# Las papas fritas pueden ser: clásicas ($2.80), con queso ($3.10) o con queso y tocineta ($3.90).
# Los helados pueden ser: de vainilla ($1.30), de fresa ($1.50) o de chocolate ($1.50).
# Las bebidas pueden ser: agua ($0.50), té frío (de durazno o limón) ($1.10) o refresco (Coca-Cola, 7-Up o Freskolita) ($0.90).

# Como output se espera:
# Deberá mostrarse de forma ordenada cada elemento del menú, con sus respectivas variaciones y precios. También se pide cuál es el producto más caro (nuggets de 30) y cuál es el más barato (agua) con su precio.

#menu_lista = [("Hamburguesas","Clásica", 4.00),("Hamburguesas","Doble Carne", 4.80), ("Hamburguesas","BBQ", 4.40),("Hamburguesas","Pollo", 4.20), ("Nuggets","15 piezas", 5.20), ("Nuggets","30 piezas", 9.50), ("Papas fritas","Clásicas", 2.80), ("Papas fritas","Queso", 3.10), ("Papas fritas""Queo y tocineta", 3.90), ("Helados","Vainilla", 1.30), ("Helados","Fresa", 1.50), ("Helados","Chocolate", 1.50), ("Bebidas","Agua", 0.50), ("Bebidas","Té","Limón", 1.10), ("Bebidas","Té","Durazno", 1.10),("Bebidas","Refresco","Coca-Cola", 0.90), ("Bebidas","Refresco","7-Up", 0.90), ("Bebidas","Refresco","Freskolita", 0.90)]

menu_lista = [("Hamburguesas","Clásica", 4.00), ("Hamburguesas","Doble Carne", 4.80), ("Hamburguesas","BBQ", 4.40), 
("Hamburguesas","Pollo", 4.20), ("Nuggets","15 piezas", 5.20), ("Nuggets","30 piezas", 9.50), 
("Papas fritas","Clásicas", 2.80), ("Papas fritas","Queso", 3.10), ("Papas fritas","Queso y tocineta", 3.90), 
("Helados","Vainilla", 1.30), ("Helados","Fresa", 1.50), ("Helados","Chocolate", 1.50), ("Bebidas","Agua", 0.50), 
("Bebidas","Té","Limón", 1.10), ("Bebidas","Té","Durazno", 1.10), ("Bebidas","Refresco","Coca-Cola", 0.90), 
("Bebidas","Refresco","7-Up", 0.90), ("Bebidas","Refresco","Freskolita", 0.90)]

def construir_diccionario_menu():
    menu = {}
    hamb = []
    nug = []
    pap = []
    hel = []
    beb = []
    te = {}
    te_l = []
    ref = {}
    ref_l = []

    for i,producto in enumerate(menu_lista):
        if producto[0] == "Hamburguesas":
            hamb.append((producto[1],producto[2]))
        elif producto[0] == "Nuggets":
            nug.append((producto[1],producto[2]))
        elif producto[0] == "Papas fritas":
            pap.append((producto[1],producto[2]))
        elif producto[0] == "Helados":
            if producto[1] == "Vainilla":
                hel.append((producto[1],producto[2]))
            elif producto[1] == "Fresa":
                hel.append(([producto[1],menu_lista[i+1][1]],producto[2]))
            else:
                pass
        else:
            if len(producto) == 3:
                beb.append((producto[1],producto[2]))
            else:
                if (producto[1] == "Té"):
                    te_l.append(producto[2])
                    te["Té"] = (te_l,producto[3])
                else:
                    ref_l.append(producto[2])
                    ref["Refresco"] = (ref_l,producto[3])
    
    beb.append(te)
    beb.append(ref)
    menu["Hamburguesas"] = hamb
    menu["Nuggets"] = nug
    menu["Papas fritas"] = pap
    menu["Helados"] = hel
    menu["Bebidas"] = beb

    return menu





#----------------------------------------
#   SE DEFINE UNA FUNCIÓN QUE IMPRIMIRÁ, DE FORMA ORDENADA, TODOS LOS ELEMENTOS DEL MENÚ CON SUS CARACTERÍSTICAS
#----------------------------------------
def mostrar_menu(menu):
    for item, variaciones in menu.items():
        print(f"{item}: ")
        if (item == "Hamburguesas") or (item == "Nuggets") or (item == "Papas fritas"):
            for variacion, precio in variaciones:
                print(f"\t- {variacion}: ${precio}")
            print("\n")
        elif (item == "Helados"):
            for variacion, precio in variaciones:
                if isinstance(variacion, list):
                    for sabor in variacion:
                        print(f"\t- {sabor}: ${precio}")
                else:
                    print(f"\t- {variacion}: ${precio}")
            print("\n")
        else:
            for variacion in variaciones:
                if isinstance(variacion, tuple):
                    print(f"\t- {variacion[0]}: ${variacion[1]}")
                else:
                    for var, var_esp in variacion.items():
                        print(f"\t- {var}:")
                        for sabor in var_esp[0]:
                            print(f"\t\t- {sabor}: ${var_esp[1]}")
                print("\n")




def mas_caro_y_barato():
    mayor = 0
    mayor_t = ()
    menor = 100
    menor_t = ()

    for producto in menu_lista:
        if producto[-1] > mayor:
            mayor = producto[-1]
            mayor_t = producto
        if producto[-1] < menor:
            menor = producto[-1]
            menor_t = producto
    

    print(f"El producto más caro es: {mayor_t[0]} - {mayor_t[1]} - ${mayor_t[-1]}")
    print(f"El producto más barato es: {menor_t[0]} - {menor_t[1]} - ${menor_t[-1]}")


def main():
    menu = construir_diccionario_menu()
    mostrar_menu(menu)
    mas_caro_y_barato()


main()