from Nodo import Nodo 

class Pila:

    def __init__(self):
        self.__primero = None
        self.__size = 0
    
    def length (self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def push(self,contenido):
        band = False
        if self.isEmpty():
            self.__primero = Nodo(None,contenido)
            band = True
            self.__size += 1
        else:
            nodo = Nodo(self.__primero,contenido)
            self.__primero = nodo
            band = True
            self.__size += 1
        return band
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            aux = self.__primero
            self.__primero = self.__primero.getSiguiente()
            self.__size -= 1
            return aux
    
    def mostrarTope(self):
        return self.__primero

    
    def recorrerLista(self):
        aux = self.__primero
        for i in range(0,self.length()):
            print(aux.getContenido())
            aux = aux.getSiguiente()
    


lista = Pila()
if lista.push(1):
    print('Se inserto con exito')

#print(lista.mostrarTope().getContenido())

if lista.push(2):
    print('Se inserto con exito')

#print(lista.mostrarTope().getContenido())

if lista.push(3):
    print('Se inserto con exito')

#print(lista.mostrarTope().getContenido())

lista.recorrerLista()

"""
eliminado = lista.eliminarPrimero()
if eliminado != None:
    print('Contenido del nodo eliminado:')
    print(eliminado.getContenido())
else:
    print('Lista vacia')

eliminado = lista.eliminarPrimero()
if eliminado != None:
    print('Contenido del nodo eliminado:')
    print(eliminado.getContenido())
else:
    print('Lista vacia')

eliminado = lista.eliminarPrimero()
if eliminado != None:
    print('Contenido del nodo eliminado:')
    print(eliminado.getContenido())
else:
    print('Lista vacia')

eliminado = lista.eliminarPrimero()
if eliminado != None:
    print('Contenido del nodo eliminado:')
    print(eliminado.getContenido())
else:
    print('Lista vacia')

print('Tope de la lista:')
print(lista.mostrarTope())
"""