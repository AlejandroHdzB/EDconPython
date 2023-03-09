class Nodo:

    __slots__ = '_next'

    def __init__(self,siguiente,contenido):
        self.siguiente = siguiente
        self.contenido = contenido
