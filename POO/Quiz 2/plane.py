#Diego Caceres 20211110856
class Plane:
    def __init__(self,id,model,type_model,travels):
        self.id = id
        self.model = model
        self.type_model = type_model
        self.travels = travels

    def show(self):
        print(f"ID: {self.id}\nModelo: {self.model}\nTipo de modelo: {self.type_model}\nViajes: {self.travels}")