#Diego Caceres 20211110856
class Person:
    def __init__(self,name,dni,nacionality):
        self.name = name
        self.dni = dni
        self.nacionality = nacionality

    def show(self):
        print(f"Nombre: {self.name}\nDNI: {self.dni}\nNacionalidad: {self.nacionality}")

class Passenger(Person):
    def __init__(self,name,dni,nacionality,type_seat,travel_id,confirmed):
        super().__init__(name,dni,nacionality)
        self.travel_id = travel_id
        self.confirmed = confirmed
        self.type_seat = type_seat
    
    def mostrar(self):
         print(f"Nombre: {self.name}\nDNI: {self.dni}\nNacionalidad: {self.nacionality}\nTipo de asiento: {self.type_seat}\nID de viaje: {self.travel_id}\nConfirmado. {self.confirmed}")

class Pilot(Person):
    def __init__(self, name, dni, nacionality,salary,plane_id):
        super().__init__(name, dni, nacionality)
        self.salary = salary
        self.plane_id = plane_id

    def mostrar(self):
        print(f"Nombre: {self.name}\nDNI: {self.dni}\nNacionalidad: {self.nacionality}\nSalario: {self.salary}\nID de avion: {self.plane_id}")