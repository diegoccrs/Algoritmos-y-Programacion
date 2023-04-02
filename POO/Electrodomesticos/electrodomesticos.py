class Electrodomestico(object):
    def __init__(self, cod_p, precio, marca, color):
        self.cod_p = cod_p
        self.precio = precio
        self.marca = marca
        self.color = color

    def view(self):
        print(("-"*30) + f"\n{self.marca}" + ("-"*30) + f"\n > Modelo: {self.cod_p}\n > Precio: {self.precio}\n > Color: {self.color}")

class Lavadora(Electrodomestico):
    def __init__(self, cod_p, precio, marca, color, capacidad):
        super().__init__(cod_p, precio, marca, color)
        self.capacidad = capacidad

    def view(self):
        print(("-"*30) + f"\n Lavadora {self.marca}\n" + ("-"*30) + f"\n > Modelo: {self.cod_p}\n > Precio: {self.precio}\n > Color: {self.color}\n Capacidad maxima de ropa: {self.capacidad}kg")

class HMicrondas(Electrodomestico):
    def __init__(self, cod_p, precio, marca, color, control):
        super().__init__(cod_p, precio, marca, color)
        self.control = control

    def view(self):
        print(("-"*30) + f"\n Microondas {self.marca}\n" + ("-"*30) + f"\n > Modelo: {self.cod_p}\n > Precio: {self.precio}\n > Color: {self.color}\n >> Control digital: {self.control}")

class Nevera(Electrodomestico):
    def __init__(self, cod_p, precio, marca, color, inc_cong, compartimientos):
        super().__init__(cod_p, precio, marca, color)
        self.inc_cong = inc_cong
        self.compartimentos = compartimientos

    def view(self):
        print(("-"*30) + f"\n Nevera {self.marca}\n" + ("-"*30) + f"\n > Modelo: {self.cod_p}\n > Precio: {self.precio}\n > Color: {self.color}\n >> Congelador incluido: {self.inc_cong}\n >> Compartimientos: {self.compartimentos} comp.")

class Licuadora(Electrodomestico):
    def __init__(self, cod_p, precio, marca, color, mat_vaso, speed):
        super().__init__(cod_p, precio, marca, color)
        self.mat_vaso = mat_vaso
        self.speed = speed

    def view(self):
        print(("-"*30) + f"\n Licuadora {self.marca}\n" + ("-"*30) + f"\n > Modelo: {self.cod_p}\n > Precio: {self.precio}\n > Color: {self.color}\n >> Material del Vaso: {self.mat_vaso}\n >> Velocidades: x{self.speed} vel.")