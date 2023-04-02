class Bebida:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class BebidaAlcoholica(Bebida):
    def __init__(self, nombre, precio,grado):
        super().__init__(nombre, precio)
        self.grado = grado

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}$\nGrado Alcoholico: {self.grado}")

class BebidaNoAlcoholica(Bebida):
    def __init__(self, nombre, precio,temperatura):
        super().__init__(nombre, precio)
        self.temperatura = temperatura

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}$\nTemperatura: {self.temperatura}")

