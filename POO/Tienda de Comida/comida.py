class Comida:
    def __init__(self,nombre,precio,valoracion):
        self.nombre = nombre
        self.precio = precio
        self.valoracion = valoracion

    def mostrar(self):
        print(f"- {self.nombre}\nPrecio: {self.precio}$\nValoracion: {self.valoracion}")

class Alimento(Comida):
    def __init__(self,nombre,precio,valoracion,tipo):
        super().__init__(nombre,precio,valoracion)
        self.tipo = tipo
    
    def mostrar(self):
        print(f"- {self.nombre}\nPrecio: {self.precio}$\nValoracion: {self.valoracion}\nTipo: {self.tipo}")

class Bebida(Comida):
    def __init__(self,nombre,precio,valoracion):
        super().__init__(nombre,precio,valoracion)

class BebidaAlcoholica(Bebida):
    def __init__(self,nombre,precio,valoracion,grados):
        super().__init__(nombre,precio,valoracion)
        self.grados = grados

    def mostrar(self):
        print(f"- {self.nombre}\nPrecio: {self.precio}$\nValoracion: {self.valoracion}\nGrados: {self.grados}")