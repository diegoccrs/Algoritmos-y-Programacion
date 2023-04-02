class Habitacion:
    def __init__(self,camas,baños,precio):
        self.camas = camas
        self.baños = baños
        self.precio =  precio

class Suite(Habitacion):
    def __init__(self, camas, baños, precio,jacuzzi):
        super().__init__(camas, baños, precio)
        self.jacuzzi = jacuzzi
    
    def mostrar(self):
          print(f"Numero de camas: {self.camas}\nNumero de baños: {self.baños}\nPrecio: {self.precio}$\nJacuzzi: {self.jacuzzi}")

class Doble(Habitacion):
    def __init__(self, camas, baños, precio,tipo):
        super().__init__(camas, baños, precio)
        self.tipo = tipo

    def mostrar(self):
        print(f"Numero de camas: {self.camas}\nNumero de baños: {self.baños}\nPrecio: {self.precio}$\nTipo de Habitacion: {self.tipo}")

class Sencilla(Habitacion):
    def __init__(self, camas, baños, precio,tv):
        super().__init__(camas, baños, precio)
        self.tv = tv

    def mostrar(self):
        print(f"Numero de camas: {self.camas}\nNumero de baños: {self.baños}\nPrecio: {self.precio}$\nTV: {self.tv}")