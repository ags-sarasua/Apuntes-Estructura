#Estructuras de datos constantes. Una vez la creamos, no la puedo modificar
#Es una estructura secuencial porque me puedo ir moviendo posición por posición
#Por ejemplo, usamos tuplas para guardar los meses del año

import sys

tupla = tuple()
lista = list()

print("Bytes de la tupla vacía: ", sys.getsizeof(tupla))
print("Bytes de la lista vacía: ", sys.getsizeof(lista))

tupla = (1,) #la coma va para que se detecte como tupla
print(type(tupla))
tupla2 = tuple("Hola")
print(tupla2)

tupla = ("String", 10, True, tupla2, [1,2,3,4,5], (9,8,7)) #Tupla compuesta+
print("Esto es una tupla: ", tupla)

#Dar vuelta la tupla:
tuplaReves = tupla[::-1]
print(tuplaReves)

#Tupla a lista
lista = list(tupla)
print("Esto es una lista: ", lista)

#Enumerar tupla (enumerar cada elemento), te da una tupla de tuplas

print(tuple(enumerate(tupla)))