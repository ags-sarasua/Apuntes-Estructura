#FIFO: el primero que llegue es el primero que se va. Entro por un extremo y salgo por el otro

class Nodo:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return "data "+ self.data

class Cola:
    def __init__(self) -> None:
        self.cola = []    