#Diego Caceres 20211110856
class Travel:
    def __init__(self,travel_id,departure_city,destination_city,schedule):
        self.travel_id = travel_id
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.schedule = schedule

    def view_info(self):
        print(f"ID de viaje: {self.travel_id}\nCiudad de salida: {self.departure_city}\nCiudad destino: {self.destination_city}\nAgenda: {self.schedule}")