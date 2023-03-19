from Nodo import Nodo

class Cola:
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__size = 0
    
    def length(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def insert(self,contenido):
        band = False
        if self.isEmpty():
            nodo = Nodo(None,contenido)
            self.__primero = nodo
            self.__ultimo = nodo
            band = True
            self.__size += 1
        else:
            nodo = Nodo(None,contenido)
            self.__ultimo.setSiguiente(nodo)
            self.__ultimo = nodo
            band = True
            self.__size += 1
        return band
        

    def delete(self):
        if self.isEmpty():
            return None
        else:
            aux = self.__primero
            self.__primero = aux.getSiguiente()
            self.__size -= 1
            return aux
 
    def seeFirst(self):
        return self.__primero

    def seeLast(self):
        return self.__ultimo

    def recorrer(self):
        aux = self.__primero
        for i in range(0,self.length()):
            print(aux.getContenido())
            aux = aux.getSiguiente()