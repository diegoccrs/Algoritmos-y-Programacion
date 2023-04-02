class Silla():
    def __init__(self,color,patas,espaldar,colchon):
        self.color = color
        self.patas = patas
        self.espaldar = espaldar
        self.colchon = colchon
    
    def show(self):
        print(f"Silla: {self.patas} {self.color} {self.espaldar} {self.colchon}")

    
    class Silla_oficina():
        def __init__(self,color,patas,espaldar,colchon,ruedas):
            self.color = color
            self.patas = patas
            self.espaldar = espaldar
            self.colchon = colchon
            self.ruedas = ruedas

        def show(self):
            print(f"Silla: {self.patas} {self.color} {self.espaldar} {self.colchon} {self.ruedas}")


