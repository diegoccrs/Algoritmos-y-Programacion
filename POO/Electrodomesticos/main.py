from electrodomesticos import *
import edd as e

edd = e.inventory()

lista = []
lista_b = []

def charge():
    for i,j in edd.items():
        for k in j:
            ex = {}
            for n,m in k.items():
                ex[n] = m
            if i.capitalize() == "Washer":
                lista.append(Lavadora(ex["cod_p"], ex["price"], ex["brand"], ex["color"], ex["capacity"]))
            if i.capitalize() == "Microwave":
                lista.append(HMicrondas(ex["cod_p"], ex["price"], ex["brand"], ex["color"], ex["digital"]))
            if i.capitalize() == "Fridge":
                lista.append(Nevera(ex["cod_p"], ex["price"], ex["brand"], ex["color"], ex["cooler"], ex["comp"]))
            if i.capitalize() == "Blender":
                lista.append(Licuadora(ex["cod_p"], ex["price"], ex["brand"], ex["color"], ex["cup"], ex["speeds"]))
            
def statcs(listas):
    temp = [0.00, [], 0]
    for i in listas:
        temp[0] = float(max(temp[0], i.precio))
        try:
            if i.capacidad:
                temp[1].append(i)
                temp[2] += 1
        except:
            pass
    print("\n>> El producto mas costoso de toda la tienda esta valuado en: ${}\n\n>> Hay un total de {} Lavadoras las cuales son:\n".format(temp[0],temp[2]))
    for i in temp[1]:
        i.view()
    print("-"*30 + "\n")
    
def delete(listas):
    printer(listas)
    while True:
        try:
            y = int(input("Cual electrodomestico desea sacar del inventario: "))
            if 0 < y and y < len(lista):
                lista_b.append(lista[y-1])
                lista.pop(y-1)
                break
            else:
                print("Objeto fuera de rango.")
        except ValueError:
            print("Valor no numerico")
        except:
            print("Error desconocido")

def printer(listas):
    for i,j in enumerate(listas, 1):
        print(("-"*30) + f"\n >> Producto: {i}")
        j.view()
    print("-"*30 + "\n")

def main():
    while True:
        try:
            x = int(input(("="*40) + ("\n Elija una opcion\n") + ("="*40) + ("\n >> 1. Productos disponibles\n >> 2. Borrar defectuoso\n >> 3. Estadisticas\n >> 4. Borrados\n\n >> 0. Salir\n\n ---> ")))
            if x == 0:
                break
            elif x == 1:
                printer(lista)
            elif x == 2:
                delete(lista)
            elif x == 3:
                statcs(lista)
            elif x == 4:
                printer(lista_b)
            else:
                print("Comando no programado")
        except ValueError:
            print("Valor no numerico")
        except:
            print("Error desconocido")

charge()
main()