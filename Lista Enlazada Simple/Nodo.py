class Nodo:

    __slots__ = ['__siguiente','__contenido']

    def __init__(self,siguiente,contenido):
        self.__siguiente = siguiente
        self.__contenido = contenido
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getContenido(self):
        return self.__contenido
    
    def setContenido(self,contenido):
        self.__contenido = contenido