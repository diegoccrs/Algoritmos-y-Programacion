class Persona(object):
    def __init__(self,cabello,estatura,genero):
        self.cabello = cabello
        self.estatura = estatura
        self.genero = genero

    def obtener(self):
        return f"{self.cabello},{self.estatura},{self.genero}"
    
    def change(self):
        x = input("Nuevo genero: ")
        if x.isalpha():
            self.genero = x