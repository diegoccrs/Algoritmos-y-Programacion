class Alumno:
    def __init__(self,nombre,grado,promedio,direccion,nombre_rep,telefono_rep):
        self.nombre = nombre
        self.grado = grado
        self.promedio = promedio 
        self.direccion = direccion
        self.nombre_rep = nombre_rep
        self.telefono_rep = telefono_rep
        self.becado = True if promedio >= 18 else False

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nGrado: {self.grado}\nPromedio: {self.promedio}\nDireccion de habitacion: {self.direccion}\nNombre del representante: {self.nombre_rep}\nTelefono del representante: {self.telefono_rep}\nBecado: {self.becado}")