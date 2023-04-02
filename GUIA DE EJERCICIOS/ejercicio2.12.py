# 2.12 CINE
# Un cine requiere un programa para calcular el precio de sus entradas y te ha contratado para realizarlo. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.

# Si el cliente es menor de 4 años puede entrar gratis
# Si tiene entre 4 y 18 años debe pagar $10
# Si es mayor de 18 años, $14
# Como output se espera:
	#Imprimir el precio correspondiente a la edad del cliente.

print("Bienvenido al cine, por favor indiquenos su edad para darle precio de su entrada")
age = int(input("Ingrese su edad: "))

if age > 0 and age < 4:
    print("Su entrada es gratuita")
elif age >= 4 and age <= 18:
    print("Su entrada tiene un valor de 10$")
elif age > 18 and age < 120:
    print("Su entrada tiene un valor de 14$")
else:
    print("Error, introduzca una edad verdadera")