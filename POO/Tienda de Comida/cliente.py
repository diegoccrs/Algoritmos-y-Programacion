class Cliente:
    def __init__(self,nombre,cedula,metodo):
        self.nombre = nombre
        self.cedula = cedula
        self.metodo = metodo

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nCedula: {self.cedula}\nMetodo de pago: {self.metodo}")