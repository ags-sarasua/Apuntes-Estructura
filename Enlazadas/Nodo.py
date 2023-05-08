"""
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "data " + self.data
"""

class Nodo():
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self) -> str:
        return str(self.dato)
    
if __name__ == "__main__":
    vagon1 = Nodo("Mango")
    print(vagon1)
    print(vagon1.prox)


    lista = [['Juan', 2], ['pepe', 8]]
    