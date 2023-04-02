class Tienda:
    def __init__(self,nombre,tipo,piso,rif,propietario,telefono):
        self.nombre = nombre
        self.tipo = tipo 
        self.piso = piso 
        self.rif = rif
        self.propietario = propietario
        self.telefono = telefono

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nTipo de tienda: {self.tipo}\nPiso: {self.tipo}\nRIF: {self.rif}\nNombre del propietario: {self.propietario}\nTelefono del propietario: {self.telefono}")