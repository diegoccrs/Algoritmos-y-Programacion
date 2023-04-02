# 9.1 SCHOOL DATABASE 
# Un colegio te ha contratado para que diseñes un programa que los ayude a almacenar de una manera más sencilla 
# toda la información de sus alumnos. 
# Cada alumno tiene nombre, grado que cursa, promedio, dirección de habitación, nombre del representante, 
# teléfono del representante y la condición de becado o no.
# Si el promedio del alumno es menor a 18, el alumno no tendrá beca; de lo contrario, sí la tendrá.
# Luego de almacenar esto en su base de datos, debe existir una función que permita ver la información organizada de cada alumno de la institución.
# Como requerimientos adicionales pidieron:
# Mostrar los nombres, grados  y promedios de las 5 personas con mejores promedios del colegio
# Mostrar un promedio general de todos los promedios de los alumnos del plantel
# Mostrar cuántos alumnos tienen promedios menores a 10, cuántos entre 10 y 15 (o sea, hasta 15.9) y cuántos entre 16 y 20.

from alumno import Alumno

def registrar_alumno(alumnos):
    nombre = input("Introduzca nombre y apellido del alumno: ").title()
    print("\n1. 1ro\n2. 2do\n3. 3ro\n4. 4to\n5. 5to\n6. 6to\n7. 7mo\n8. 8vo\n9. 9no\n10. 4to año\n11. 5to año\n")
    grado = input("Introduzca el grado que cursa el alumno: ")
    while not grado.isnumeric() or int(grado) not in range(1,12):
        grado = input("Por fvor ingrese un valor valido: ")
    if int(grado) == 1:
        grado = "1ro"
    elif int(grado) == 2:
        grado = "2do"
    elif int(grado) == 3:
        grado = "3ro"
    elif int(grado) == 4:
        grado = "4to"
    elif int(grado) == 5:
        grado = "5to"
    elif int(grado) == 6:
        grado = "6to"
    elif int(grado) == 7:
        grado = "7mo"
    elif int(grado) == 8:
        grado = "8vo"
    elif int(grado) == 9:
        grado = "9no"
    elif int(grado) == 10:
        grado = "4to año"
    else:
        grado = "5to año"

    promedio = float(input("Ingrese promedio del alumno: "))
    direccion = input("Ingrese la direccion de habitacion del alumno: ").capitalize()
    nombre_rep = input("Ingrese el nombre del representante del alumno: ").title()
    telefono_rep = int(input("Ingrese numero de telefono del representante (sin espacios ni caracteres especiales): "))
    
    nuevo_alumno = Alumno(nombre,grado,promedio,direccion,nombre_rep,telefono_rep)
    alumnos.append(nuevo_alumno)

    
    print("\nAlumno registrado con exito")
    nuevo_alumno.mostrar()

def ver_alumnos(alumnos):
    for valor,alumno in enumerate(alumnos):
        print("---",valor+1,"----------")
        alumno.mostrar()

def top_5(alumnos):
    alumnos.sort(key = lambda alumno: alumno.promedio, reverse = True)
    for valor,alumno in enumerate(alumnos):
        if valor < 5:
            print("---",valor+1,"---------")
            print(alumno.mostrar())

def promedio_general(alumnos):
    promedios = []
    for alumno in alumnos:
        promedios.append(alumno.promedio)

    promedio_promedios = sum(promedios)/len(promedios)
    print(f"El promedio general del colegio es {promedio_promedios} puntos")

def clasificar_por_promedio(alumnos):
    menores_a_10 = 0
    entre_10_y_16 = 0
    entre_16_y_20 = 0

    for alumno in alumnos:
        if alumno.promedio < 10:
            menores_a_10 += 1
        elif alumno.promedio > 10 and alumno.promedio < 16:
            entre_10_y_16 += 1
        else:
            entre_16_y_20 += 1

    print(f"Cantidad de alumnos con promedios menores a 10: {menores_a_10}\nCantidad de alumnos con promedios entre 10 y 15.9: {entre_10_y_16}\nCantidad de alumnos con promedios entre 16 y 20: {entre_16_y_20}")

def main():
    alumnos = []
    print("*Bienvenido a la Base de Datos de Estudiantes*")
    while True:
        print("1- Registrar alumno\n2- Ver estudiantes registrados\n3- Ver mejores 5 promedios\n4- Ver promedio general\n5- Ver cantidad de alumnos por promedio\n")
        seleccion = input("Seleccione una accion a realizar: ")
        while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
            seleccion = input("Porfavor ingrese un valor valido: ")
        if int(seleccion) == 1:
            registrar_alumno(alumnos)
        elif int(seleccion) == 2:
            ver_alumnos(alumnos)
            if len(alumnos) == 0:
                print("Todavia no hay alumnos registrados")
        elif int(seleccion) == 3:
            top_5(alumnos)
            if len(alumnos) == 0:
                print("Todavia no hay alumnos registrados")
        elif int(seleccion) == 4:
            promedio_general(alumnos)
            if len(alumnos) == 0:
                print("Todavia no hay alumnos registrados")
        elif int(seleccion) == 5:
            clasificar_por_promedio(alumnos)

        otro = input("\n¿Desea realizar otra operacion? (S para si, N para no): ")
        while otro.upper() != "S" and otro.upper() != "N":
            otro = input("Por favor ingrese un valor valido: ")
        if otro.upper() == "S":
            continue
        else:
            break

main()