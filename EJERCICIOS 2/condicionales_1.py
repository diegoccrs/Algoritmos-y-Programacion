#La pizzeria Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación: 
# Ingredientes vegetarianos: Pimiento y Tofu
# Ingredientes no vegetarianos: Peperoni, Jamon, Salmón
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menu con los ingredientes disponibles para que elija. 
# Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate que estan en todas las pizzas. 
# Al final de debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzeria Bella Napoli \n\t1-Pizza Vegetariana\n\t2-Pizza no vegetariana")

pizza = int(input("¿Que tipo de pizza desea? "))

if pizza == 1:
    print("Ingredientes: \n\t1-Pimiento\n\t2-Tofu")
    ingrediente1 = int(input("¿Que ingrediente desea? "))
    if ingrediente1 == 1:
        print("Has escogido Pizza Vegetariana con Pimiento")
    elif ingrediente1 ==  2:
        print("Has escogido Pizza Vegetariana con Tofu")
    else:
        print("ERROR")
elif pizza == 2:
    print("Ingredientes: \n\t1-Peperoni\n\t2-Jamon\n\t3-Salmon")
    ingrediente2 = int(input(("¿Que ingrediente desea? ")))
    if ingrediente2 == 1:
        print("Has escogido Pizza no Vegetariana con Peperoni")
    elif ingrediente2 == 2:
        print("Has escogido Pizza no vegetariana con Jamon")
    elif ingrediente2 == 3:
        print("Pizza no vegetariana con Salmon")
    else:
        print("ERROR")
else:
    print("ERROR")