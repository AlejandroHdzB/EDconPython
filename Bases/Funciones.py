def buscar(item,lista):
    cont = 0
    for i in lista:
        if item == i:
            cont+=1
    return cont

letras = ('a','b','c','d','d','a')

print(buscar('d',letras))