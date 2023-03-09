class Pila:
    def __init__(self):
        self.pila = []
    
    def isEmpty(self):
        return True if self.pila == [] else False
    
    def push(self,elemento):
        self.pila.append(elemento)

    def pop(self):
        return self.pila.pop()
    
    def size(self):
        return len(self.pila)
    
    def lastElement(self):
        return self.pila[len(self.pila)-1]