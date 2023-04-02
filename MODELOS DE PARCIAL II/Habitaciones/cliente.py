class Cliente:
    def __init__(self,nombre,edad,id,telefono,acompañantes):
        self.nombre = nombre
        self.edad = edad
        self.id = id
        self.telefono = telefono
        self.acompañantes = acompañantes

    def mostrar(self):
        print(f"Noombre: {self.nombre}\nEdad: {self.edad}\nCedula: {self.id}\nTelefono: {self.telefono}\nAcompañantes: {self.acompañantes}")