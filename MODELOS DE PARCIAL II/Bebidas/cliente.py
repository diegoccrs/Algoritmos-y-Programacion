class Cliente:
    def __init__(self,nombre,edad,id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCedula: {self.id}")