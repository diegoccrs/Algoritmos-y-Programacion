class Cliente:
    def __init__(self,nombre,edad,id,telefono):
        self.nombre = nombre
        self.edad = edad
        self.id = id
        self.telefono = telefono

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCedula: {self.id}\nNumero de telefono: {self.telefono}")
        
        