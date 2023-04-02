# 2.1 REGISTRO DE DATOS BASICO
# Realice un algoritmo que pida el nombre de un alumno, apellido, cédula, altura, peso, BMI
# (Body Mass Index), deporte favorito y promedio de sus calificaciones en su último periodo
# estudiantil.

# Como output se espera:
# Imprimir los datos en pantalla.

name = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
id = int(input("Ingrese su cedula: "))
height = float(input("Ingrese su altura: "))
weight = float(input("Ingrese su peso: "))
bmi = int(input("Ingrese su BMI: "))
favorite = input("Ingrese su deporte favorito: ")
promedio = float(input("Ingrese su promedio estudiantil: "))

print("Nombre: ",name)
print("Apellido: ",apellido)
print("Cedula: ",id)
print("Altura: ",height)
print("Peso: ",weight)
print("BMI: ",bmi)
print("Deporte Favorito: ",favorite)
print("Promedio: ",promedio)