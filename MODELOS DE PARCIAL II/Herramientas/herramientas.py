class Herramienta:
    def __init__(self,marca,color,precio,tipo):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.tipo = tipo 

class Plomeria(Herramienta):
    def __init__(self,marca,color,precio,tipo,pulgadas,ajustable,mantenimiento):
        super().__init__(marca,color,precio,tipo)
        self.pulgadas = pulgadas
        self.ajustable = ajustable
        self.mantenimiento = mantenimiento

    def show(self):
         print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}$\nTipo: {self.tipo}\nPulgadas: {self.pulgadas}\nAjustable: {self.ajustable}\nMantenimiento: {self.mantenimiento}")

class Herreria(Herramienta):
    def __init__(self, marca, color, precio, tipo,grados):
        super().__init__(marca, color, precio, tipo)
        self.grados = grados

    def show(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}$\nTipo: {self.tipo}\nGrados: {self.grados}")

class Carpinteria(Herramienta):
    def __init__(self, marca, color, precio, tipo,garantia):
        super().__init__(marca, color, precio, tipo)
        self.garantia = garantia

    def show(self):
        print(f"Marca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}$\nTipo: {self.tipo}\nGarantia: {self.garantia}")