#Diego Caceres 20211110856
from person import *
from plane import *
from travel import *
import edd as e

edd = e.inventory()

lista_pasajeros = []
lista_pilotos = []
lista_aviones = []
lista_viajes = []

def agarrar_datos():
    for i,j in edd.items():
        for k in j:
            dic = {}
            for w,m in k.items():
                dic[w] = m
            if i == "passengers":
                lista_pasajeros.append(Passenger(dic["name"], dic["dni"], dic["nacionality"], dic["t_seat"], dic["travel_id"], dic["p_confirmed"]))
            if i == "pilots":
                lista_pilotos.append(Pilot(dic["name"], dic["dni"], dic["nacionality"], dic["salary"], dic["plane_id"]))
            if i == "plane":
                lista_aviones.append(Plane(dic["id"], dic["model"], dic["t_model"], dic["flights"]))
            if i == "travel":
                lista_viajes.append(Travel(dic["travel_id"], dic["dep_city"], dic["des_city"], dic["scheculed"]))

def ver_pasajeros(lista_pasajeros):
    for i,j in enumerate(lista_pasajeros):
        print("-"*20, i+1, "-"*20)
        j.mostrar()

def ver_itinerario(lista_aviones):
    for i,j in enumerate(lista_aviones):
        print("-"*20, i+1, "-"*20)
        j.show()

def menu():
    print("BIENVENIDO A MANGO AIRLINES\n")
    while True:
        print("1. Ver pasajeros\n2. Ver itinerario de los aviones\n3. Confirmar documentos de viaje\n4. Salir\n")
        seleccion = int(input("Ingrese una opcion: "))
        if seleccion == 1:
            ver_pasajeros(lista_pasajeros)
        elif seleccion == 2:
            ver_itinerario(lista_aviones)
        elif seleccion == 3:
            pass
        elif seleccion == 4:
            break
        else:
            print("Error, por favor vuelva a intentar con valores validos ")

agarrar_datos()
menu()