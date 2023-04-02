# 2.4 CALCULADORA 
# Diseña un programa que permita realizar las siguientes operaciones matemáticas:
# Suma
# Resta
# Multiplicación
# División
# Potencia
# Módulo
# Comparar (mayor o menor que)
# Valor absoluto
# Debe preguntarse qué operación se desea hacer y tomarse dos números por teclado (excepto para valor absoluto). 
# Finalmente, imprime el resultado.

print("Hola")
print("Bienvenido a la calculadora")
print("Operaciones: \n\t1-Suma\n\t2-Resta\n\t3-Multiplicacion\n\t4-Division\n\t5-Potencia\n\t6-Modulo\n\t7-Comparacion (mayor o menor que)")

operation = int(input("Que operacion desea realizar: "))

if operation == 1:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1+n2)
elif operation == 2:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1-n2)
elif operation == 3:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1*n2)
elif operation == 4:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1/n2)
elif operation == 5:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1**n2)
elif operation == 6:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    print("Resultado: ",n1%n2)
elif operation == 7:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    if n1 > n2:
        print(n1,"es mayor que",n2)
    elif n1 < n2:
        print(n1,"es menor que",n2)
    else:
        print("Los numeros son iguales")
elif operation == 8:
    n1 = int(input("Ingrese un numero: "))
    print("Resultado: ",n1)
else:
    print("Error, el numero introducido no es valido")