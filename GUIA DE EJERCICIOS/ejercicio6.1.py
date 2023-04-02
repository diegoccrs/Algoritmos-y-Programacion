# 6.1 ESTUDIO DEMOGRAFICO
# Se ha realizado un estudio demográfico en una urbanización y se te ha solicitado que
# A partir de los datos obtenidos (almacenados en un diccionario de diccionarios), calcules las siguientes estadísticas:

# Cantidad total de residentes de la urbanización.
# Promedio de edad por género.
# Nombre y edad de la persona más joven.
# Nombre y edad de la persona más vieja.
# Cantidad de personas según su ocupación.

# Output:
# Total residentes: 37
# Promedio edades:
# H: 44
# M: 45
# Persona más joven: Luisana González, 5 año(s).
# Persona más vieja: Valerio Fiore, 97 año(s).
# Cantidad según ocupación:

# Médicos: 6
# Profesores: 4
# Ingenieros: 4
# Administradores: 4

# Psicólogos: 3
# Abogados: 5
# Desempleados: 4
# Estudiantes: 7

residentes = {
    "Julia Rodríguez": {"Edad": 21, "Género": "M","Ocupación": "Estudiante"}, 
    "Santiago López": {"Edad": 33, "Género": "H", "Ocupación": "Abogado"}, 
    "Luis González": {"Edad": 8, "Género": "H", "Ocupación": "Estudiante"}, 
    "Luisana González": {"Edad": 5, "Género": "M", "Ocupación": "Estudiante"}, 
    "Martina Reverón de González": {"Edad": 37, "Género": "M", "Ocupación": "Ingeniero"}, 
    "Sergio González": {"Edad": 37, "Género": "H", "Ocupación": "Ingeniero"}, 
    "Abel Araujo": {"Edad": 81, "Género": "H", "Ocupación": "Médico"}, 
    "Roberto Mendoza": {"Edad": 56, "Género": "H", "Ocupación": "Profesor"}, 
    "Bárbara Zapatero de Piñera": {"Edad": 32, "Género": "M", "Ocupación": "Psicólogo"}, 
    "Leonardo Piñera": {"Edad": 31, "Género": "H", "Ocupación": "Administrador"}, 
    "Gustavo Álvarez": {"Edad": 14, "Género": "H", "Ocupación": "Estudiante"}, 
    "Guillermo Álvarez": {"Edad": 38, "Género": "H", "Ocupación": "Médico"}, 
    "Laura Paz de Álvarez": {"Edad": 38, "Género": "M", "Ocupación": "Desempleado"}, 
    "Ignacio Salcedo": {"Edad": 19, "Género": "H", "Ocupación": "Estudiante"}, 
    "Saúl Salcedo": {"Edad": 22, "Género": "H", "Ocupación": "Estudiante"}, 
    "Romina Salcedo": {"Edad": 25, "Género": "M", "Ocupación": "Administrador"}, 
    "Elena Pinto de Salcedo": {"Edad": 52, "Género": "M", "Ocupación": "Abogado"}, 
    "Mauricio Salcedo": {"Edad": 52, "Género": "H", "Ocupación": "Ingeniero"}, 
    "Tatiana Echeverría": {"Edad": 68, "Género": "M", "Ocupación": "Médico"}, 
    'Marcelo Gonçalves': {"Edad": 27, "Género": "H", "Ocupación": "Administrador"}, 
    "Jessica Franco de Gonçalves": {"Edad": 26, "Género": "M", "Ocupación": "Profesor"}, 
    "Valerio Fiore": {"Edad": 97, "Género": "H", "Ocupación": "Desempleado"}, 
    "Giuliana Rossi de Fiore": {"Edad": 95, "Género": "M", "Ocupación": "Desempleado"}, 
    "José Castro": {"Edad": 35, "Género": "H", "Ocupación": "Abogado"}, 
    "Samantha Correa de Castro": {"Edad": 35, "Género": "M", "Ocupación": "Abogado"}, 
    "Ángel Castro": {"Edad": 7, "Género": "H", "Ocupación": "Estudiante"}, 
    "Antonieta Marín": {"Edad": 58, "Género": "M", "Ocupación": "Profesor"}, 
    "Lorenzo Blanco": {"Edad": 77, "Género": "H", "Ocupación": "Abogado"}, 
    "Vanessa Blanco de Bustamante": {"Edad": 37, "Género": "M", "Ocupación": "Médico"}, 
    "Raúl Bustamante": {"Edad": 39, "Género": "H", "Ocupación": "Médico"}, 
    "Carolina Alcalá": {"Edad": 24, "Género": "M", "Ocupación": "Ingeniero"}, 
    "Juan Alcalá": {"Edad": 60, "Género": "H", "Ocupación": "Psicólogo"}, 
    "Ingrid Gil de Alcalá": {"Edad": 60, "Género": "M", "Ocupación": "Profesor"}, 
    "Francesca Costa de Gil": {"Edad": 88, "Género": "M", "Ocupación": "Médico"}, 
    "Giancarlo Gil": {'Edad': 89, "Género": "H", "Ocupación": "Psicólogo"}, 
    "César Lovera": {"Edad": 64, "Género": "H", "Ocupación": "Administrador"}, 
    "Natalia Lovera": {"Edad": 64, "Género": "M", "Ocupación": "Desempleado"}
    }


edades_hombres = []
promedio_edades_hombres = 0
edades_mujeres = []
promedio_edades_mujeres = 0





#-------------------------------------------------------------------
#    FUNCIÓN PARA PROMEDIAR EDADES
#-------------------------------------------------------------------
def promediar_edades():

    #    SE RECORRE EL DICCIONARIO DE DICCIONARIOS CON UN FOR LOOP

    for persona,datos in residentes.items():

        #   SE SEPARAN LAS EDADES POR GÉNERO Y SE AGREGAN A UNA     LISTA SEGÚN CONVENGA

        if datos["Género"] == "M":
            edades_mujeres.append(datos["Edad"])
        else:
            edades_hombres.append(datos["Edad"])


    #   AHORA SE SABE CUÁNTOS HOMBRES Y CUÁNTAS MUJERES HAY, YA SE PUEDE CALCULAR EL PROMEDIO

    promedio_edades_mujeres = sum(edades_mujeres)//len(edades_mujeres)
    promedio_edades_hombres = sum(edades_hombres)//len(edades_hombres)
    print(f"Promedio edades:\n\t- Mujeres: {promedio_edades_mujeres}\n\t- Hombres:{promedio_edades_hombres}")














#-------------------------------------------------------------------
#    FUNCIÓN PARA BUSCAR PERSONA MÁS JOVEN Y MÁS VIEJA
#-------------------------------------------------------------------
def buscar_menor_y_mayor():
    menor = 100
    menor_n = ""
    mayor = 0
    mayor_n = ""

    #    SE RECORRE EL DICCIONARIO DE DICCIONARIOS CON UN FOR LOOP PARA CONSEGUIR A LA PERSONA MÁS VIEJA Y MÁS JÓVEN

    for persona,datos in residentes.items():
        if datos["Edad"] < menor:
            menor = datos["Edad"]
            menor_n = persona
        if datos["Edad"] > mayor:
            mayor = datos["Edad"]
            mayor_n = persona

    print(f"Persona más joven: {menor_n}, {menor} año(s).")
    print(f"Persona más vieja: {mayor_n}, {mayor} año(s).")

            







#-------------------------------------------------------------------
#    FUNCIÓN PARA CONTAR PERSONAS POR OCUPACIÓN
#-------------------------------------------------------------------
def contar_ocupacion():
    medicos = 0
    profesores = 0
    ingenieros = 0
    administradores = 0
    psicologos = 0
    abogados = 0
    desempleados = 0
    estudiantes = 0

    #    SE RECORRE EL DICCIONARIO DE DICCIONARIOS CON UN FOR LOOP

    for persona,datos in residentes.items():

        #    SEGÚN LA OCUPACIÓN DE LA PERSONA, SE ACTUALIZA EL CONTADOR CORRESPONDIENTE

        if datos["Ocupación"] == "Médico":
            medicos += 1
        elif datos["Ocupación"] == "Profesor":
            profesores += 1
        elif datos["Ocupación"] == "Ingeniero":
            ingenieros += 1
        elif datos["Ocupación"] == "Administrador":
            administradores += 1
        elif datos["Ocupación"] == "Psicólogo":
            psicologos += 1
        elif datos["Ocupación"] == "Abogado":
            abogados += 1
        elif datos["Ocupación"] == "Desempleado":
            desempleados += 1
        else:
            estudiantes += 1
    
    print(f"Cantidad según ocupación:\n\t- Médicos: {medicos}\n\t- Profesores: {profesores}\n\t- Ingenieros: {ingenieros}\n\t- Administradores: {administradores}\n\t- Psicólogos: {psicologos}\n\t- Abogados: {abogados}\n\t- Desempleados: {desempleados}\n\t- Estudiantes: {estudiantes}")














def main():

    #-------------------------------------------------------------------
    #    RESPUESTA DE LA PRIMERA PREGUNTA
    #-------------------------------------------------------------------
    print(f"Total residentes: {len(residentes)}")


    #función para promedio de edades
    promediar_edades()

    #función para menor y mayor
    buscar_menor_y_mayor()
        
    #funcion para contar personas por ocupacion
    contar_ocupacion()





main()