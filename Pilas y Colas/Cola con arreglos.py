class Cola:
    def __init__(self):
        self.cola = []

    def isEmpty(self):
        return True if self.cola == [] else False
    
    def addElement(self,elemento):
        self.cola.insert(0,elemento)

    def popElement(self):
        return self.cola.pop()
    
    def size(self):
        return len(self.cola)
    
    def seeStart(self):
        return self.cola[len(self.cola)-1]
    
    def seeLast(self):
        return self.cola[0]