class Coches:
    def __init__(self,gas):
        self.gas = gas
        
    def verGasolina(self):
        print(self.gas)

coche1 = Coches(5)
coche1.verGasolina()