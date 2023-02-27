class Instrumento:
    def __init__(self,precio):
        self.precio = precio
    
    def tocar(self):
        print("Music")

class Guitarra(Instrumento):
    def __init__(self, precio,tipo):
        super().__init__(precio)
        self.tipo = tipo

class Acuatico:
    def nada(self):
        print("Nada")

class Terrestre:
    def camina(self):
        print("Camina")

class Cocodrilo(Acuatico,Terrestre):
    pass

cocodrilo = Cocodrilo()

cocodrilo.camina()
cocodrilo.nada()