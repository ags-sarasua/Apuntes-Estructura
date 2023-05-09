from collections import deque

stack = deque(maxlen=2) #importo métodos
stack1 = deque() #esta es de backup, idem listas

stack.append(3)
stack.append(33)
print(stack)

#Para eliminar el último elemento que ingresó
stack1.apend(stack.pop()) #Ojo, eliminar elementos de una lista vacía produce error
print(stack)
stack.append(4)
print(stack)
stack.append(44) #Si le agrego más que la cantidad máxima de elementos, se borran los más viejos
print(stack)