#Vemos el sistema LIFO, el último que entra queda arriba de todo y es el 1ero que sale
#Usamos la pila si tenemos una pila de documentos y necesitamos guardarlos tal cual está


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class pilaLinkedlist:
    def __init__(self, headvalue = None):
        self.headvalue = headvalue

#Pila como lista simple:
lista = []
lista.append(38)
lista.append(14)
lista.append(7)
print(lista)

#Eliminar elementos
print(lista.pop())

#Para no perder los elementos usamos una lista auxiliar
pilaAux = []
pilaAux.append(lista.pop())
pilaAux.append(lista.pop())
pilaAux.append(lista.pop()) #Listo ahi sacamos todos los elementos
print(pilaAux) #pero está al revés el orden ahora
pilaAux.reverse()


