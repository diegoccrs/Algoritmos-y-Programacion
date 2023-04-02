# Te han contratado para que diseñes un algoritmo en Python que lleve el registro de las entradas y salidas de los empleados 
# de una compañía a los distintos departamentos del edificio. 
# Dichos departamentos se encuentran reflejados en el siguiente diccionario:
   
#edificio={
   #"Marketing": [ ],
   #"Recursos humanos": [ ],
   #"Contabilidad": [ ],
   #"Ventas": [ ],
#}

# El software debe contar con estas funcionalidades:

# Ingreso al edificio: Se requiere agregar a la base de datos planteada anteriormente los datos de la persona 
# que está entrando al edificio (nombre, apellido, edad y cédula). 
# Los datos de esta persona deben ubicarse dentro de la lista correspondiente al departamento al que se dirija. 
# Por ejemplo, si Pedro Perez entra al edificio y se dirige al departamento de marketing, el diccionario se vería así:

#edificio={
   #"Marketing": [ { “Nombre”: “Pedro”, “Apellido”: “Perez", “Edad”: 24, “Cédula”: 26123456 }, ],
    #"Recursos humanos": [ ],
   #"Contabilidad": [ ],
   #"Ventas": [ ],
#}

#RECORDATORIO: Las cédulas de identidad son únicas para cada persona, por ende, 
# no pueden haber dos personas o más con la misma cédula dentro del edificio.

# Salida del edificio: Se requiere eliminar a la persona que se desee de la lista en la que se encuentra.

# TIP: Para eliminar a una persona en particular, hacerlo ingresando algún valor que sea único de esa persona.

# Estadísticas: Se requiere mostrar por pantalla en un output amigable e intuitivo al usuario las siguientes estadísticas:
# Cuántas personas hay en cada departamento.
# Cuántas hay en total en el edificio.
# BONO (3 puntos extras. 1.5 c/u):
# Cuál es el promedio de edad de las personas en cada departamento.
# Cuál es el promedio de edad de las personas en el edificio. 

# REQUERIMIENTOS DEL ALGORITMO

# Contar con un menú que permita al usuario seleccionar la acción a realizar.
# Validar inputs: 
# El nombre y el apellido deben ser de tipo string con solo caracteres alfabéticos.
# La cédula y la edad debe tener solo caracteres numéricos y enteros.
# Y cualquier otro input utilizado debe ser tolerante a ingresos inválidos.
# Volver al menú inicial al finalizar cada operación, y permitir al usuario cerrar el programa cuando lo desee.

edificio = {
   "Marketing": [ ],
   "Recursos humanos": [ ],
   "Contabilidad": [ ],
   "Ventas": [ ],
}

# Menú
while True:
    # La lista con las opciones para mostrar al usuario
    opciones = ['Ingreso al edificio', 'Salida del edificio', 'Estadisticas', 'Bono', 'Salir']
    
    # Se muestran las opciones una a una al usuario junto al índice para que seleccione una
    for index, opcion in enumerate(opciones):
        print(f'{index + 1}.{opcion}')
    
    # El usuario va a elegir una de las opciones
    seleccionar_opcion = input('Seleccione una opcion: ')
    # Validación: que sea un numero y que la opcion que escoja esté dentro de las opciones que se le muestran
    while not seleccionar_opcion.isnumeric() or int(seleccionar_opcion) - 1 not in range(0, len(opciones)):
        print('Valide sus datos')
        seleccionar_opcion = input('Seleccione una opcion: ')
    seleccionar_opcion = int(seleccionar_opcion) - 1

    # Ingreso al edificio
    if seleccionar_opcion == 0:
        # Obtener cedula
        cedula = input('Ingrese la cédula: ')
        # Validación: que sea un numero y que no sea menor igual a 0
        while not cedula.isnumeric() or int(cedula) <= 0:
            print('Valide sus datos')
            cedula = input('Ingrese la cédula: ')
        cedula = int(cedula)

        # Buscamos si la persona ya existe, lo hacemos comparando cedulas en los distintos departamentos del edificio
        encontrado = False
        for key, departamento in edificio.items():
            for index, persona in enumerate(departamento):
                if persona['cedula'] == cedula:
                    encontrado = True
        
        # Validamos para que no continue si existe la persona en el edificio
        if encontrado:
            print('¡La persona ya se encuentra registrada!')
            continue

        # Obtener el key_departamento
        # Se muestran los departamentos uno a uno al usuario junto al índice para que seleccione uno
        for index, key_departamento in enumerate(edificio):
            print(f'{index + 1}. {key_departamento}')

        # El usuario va a elegir uno de los departamentos
        seleccionar_departamento = input('Seleccione un departamento: ')
        # Validación: que sea un numero y que el departamento que escoja esté dentro de los departamentos que se le muestran
        while not seleccionar_departamento.isnumeric() or int(seleccionar_departamento) - 1 not in range(0, len(edificio)):
            print('Valide sus datos')
            seleccionar_departamento = input('Seleccione un departamento: ')
        seleccionar_departamento = int(seleccionar_departamento) - 1

        # Obtener nombre
        nombre = input('Ingrese el nombre: ')
        # Validación: que no esté vacio y que el contenido sea alfabético (sin numeros ni caracteres especiales)
        while nombre == ' ' or not nombre.replace(' ', '').isalpha():
            print('Valide sus datos')
            nombre = input('Ingrese el nombre: ')

        # Obtener apellido
        apellido = input('Ingrese el apellido: ')
        # Validación: que no esté vacio y que el contenido sea alfabético (sin numeros ni caracteres especiales)
        while apellido == ' ' or not apellido.replace(' ', '').isalpha():
            print('Valide sus datos')
            apellido = input('Ingrese el apellido: ')

        # Obtener edad
        edad = input('Seleccione la edad: ')
        # Validación: que sea un numero y que no sea menor a 0
        while not edad.isnumeric() or int(edad) < 0:
             print('Valide sus datos')
             edad = input('Seleccione la edad: ')
        edad = int(edad)

        # Creamos la persona como un diccionario con todos los datos que nos pidieron en el enunciado
        persona = {'nombre': nombre, 'apellido': apellido, 'cedula': cedula, 'edad': edad}

        # Buscamos el departamento donde el usuario quiere que sea añadido la persona usando seleccionar_departamento
        for index, key_departamento in enumerate(edificio):
            if seleccionar_departamento == index:
                # Cuando encontremos el key_departamento que corresponde a la selección del usuario entonces añadimos
                # a la lista del departamento a la persona
                edificio[key_departamento].append(persona)

        print('¡Se ha añadido exitosamente a la persona!') 

    # Salida del edificio
    elif seleccionar_opcion == 1:
        # Obtener cedula
        cedula = input('Ingrese la cedula: ')
        # Validación: que sea un numero y que no sea menor igual a 0
        while not cedula.isnumeric() or int(cedula) <= 0:
            print('Valide sus datos')
            cedula = input('Ingrese la cedula: ')
        cedula = int(cedula)

        # Buscamos si la persona ya existe, lo hacemos comparando cedulas en los distintos departamentos del edificio
        encontrado = False
        for key, departamento in edificio.items():
            for index, persona in enumerate(departamento):
                if persona['cedula'] == cedula:
                    encontrado = True
                    # Cuando encontremos a la persona entonces la eliminamos de la lista del departamento donde se encuentre
                    # de la siguiente forma:
                    departamento.pop(index)              
        
        if encontrado:
            print('¡Se ha eliminado exitosamente a la persona!')
        else:
            print('¡No se ha encontrado a la persona!')
            

    # Estadisticas
    elif seleccionar_opcion == 2:
        total = 0
        # Cuántas personas hay en cada departamento.
        for key, departamento in edificio.items():
            # Sumamos en total la cantidad de personas que hay en cada departamento para obtener
            # el total de personas en el edificio
            total += len(departamento)
            print(f'En el departamento {key} hay {len(departamento)} personas.')

        # Cuántas hay en total en el edificio.
        print(f'En el edificio hay {total} personas.')

        
    # Bono
    elif seleccionar_opcion == 3:
        # Sin comentar: analicen que pasa en cada caso y si tienen dudas me pueden escribir :)

        sum_edad_edificio = 0
        personas_edificio = 0

        # Cuál es el promedio de edad de las personas en cada departamento.
        for key, departamento in edificio.items():
            sum_edad = 0
            personas_departamento = len(departamento)

            if personas_departamento == 0:
                continue

            for persona in departamento:
                sum_edad += persona['edad']
        
            promedio_departamento = sum_edad / personas_departamento
            print(f'El departamento {key} las personas tienen un promedio de edad de {promedio_departamento}.')
            
            sum_edad_edificio += sum_edad
            personas_edificio += personas_departamento

        # Cuál es el promedio de edad de las personas en el edificio.
        if personas_edificio == 0:
            print('No se han registrado personas en el edificio')
            continue

        promedio_edificio = sum_edad_edificio / personas_edificio
        print(f'En el edificio hay {personas_edificio} persona(s) y hacen un promedio de edad de {promedio_edificio}')

    else:
        break

print('¡¡¡Adios!!!')