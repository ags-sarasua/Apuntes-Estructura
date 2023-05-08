#Vemos el sistema LIFO, el último que entra queda arriba de todo y es el 1ero que sale
#Usamos la pila si tenemos una pila de documentos y necesitamos guardarlos tal cual está


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class pilaLinkedlist:
    def __init__(self, headvalue = None):
        self.headvalue = headvalue

#FIFO: el primero que llegue es el primero que se va. Entro por un extremo y salgo por el otro