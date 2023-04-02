# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Tabla: Fruta:    Precio:
        #Platano  1.35
        #Manzana  0.80
        #Pera     0.85
        #Naranja  0.70

prices = {"Platano": 1.35, "Manzana": 0.80,"Pera": 0.85,"Naranja": 0.70}

fruit = input("¿Que fruta desea? ").title()
kilos = int(input("Ingrese el numero de kilos: "))

if fruit in prices:
    print(f"{kilos} kilogramos de {fruit} valen {prices[fruit]*kilos} $")
else:
    print(f"La fruta {fruit} no esta disponible")