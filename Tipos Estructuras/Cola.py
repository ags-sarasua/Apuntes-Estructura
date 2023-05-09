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

from collections import deque

deques = deque()
deques.append(8)
deques.append(88)
deques.append(888)
print(deques)
#Ahora, el primero en salir es el primero en entrar... en este caso el 8
deques.popleft()
print(deques)

#Las colas también pueden implementarse con listas
cola=[]
cola.insert(0,9)
print(cola)
cola.insert(0,99)
cola.insert(0,999)
print(cola)

cola.pop()
cola.pop()
cola.pop()
print(cola)
