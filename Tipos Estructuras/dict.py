"""Dinámico, se maneja de a pares clave-valor. No se pueden repetir los elementos
"""
import os.path
from xml.dom import NoModificationAllowedErr 
from random import *

#Vamos a necesitar la clase persona

class Persona():
    def __init__(self, nombre, indent, edad, sexo):
        self.nombre = nombre
        self.indent = indent
        self.edad = edad
        self.sexo = sexo
    
    def __str__(self):
        cadena = ""
        cadena = "La persona llamada {} tiene DNI {}, su edad es {}".format(self.nombre, self.indent, self.edad)
        return cadena
    
    def mayor_edad(self):
        return self.edad >= 21

#Creamos un par de personas
ninfa=Persona("Ninfa", 111222, 20, "F")
dana=Persona("Dana", 333444, 21, "F")
pedro=Persona("Pedro", 555666, 30, "M")

#Primera forma de crear un diccionario 
diccionario1 = {1: "Micho", 2: "Tito", 3: "Negro", 4: "Gordo"}
diccionario2 = dict()

#Agregar datos, le damos diccionario["key"]=Dato
diccionario2["Ninfa"]=ninfa
diccionario2["Dana"]=dana
diccionario2["Pedo"]=pedro

print(diccionario1)
print(diccionario2)
print(diccionario2["Ninfa"])

#Cuando quiero ver la información de un diccionario, uso keys, values o items
elementos = diccionario1.items()
print(elementos)
llaves = diccionario1.keys()
print(llaves)
valores = diccionario1.values()
print(valores)

#Formas de movernos
print("Forma de movernos")
for key, value in diccionario1.items():
    print(key, value)

#Crear un diccionario a partir de una lista
clientes=["Elber", "Galarga", "Nacho", "Tacorta"]
dicc_clientes = {cliente: randint(1, 20) for cliente in clientes}
print(dicc_clientes.items())

#Otra forma
dicc_clientes2 = {}
for cliente in clientes:
        dicc_clientes2[cliente] = randint(1, 140)
print(dicc_clientes2.items())

#Crear un diccionario filtrando desde la lista
#dic3 = {cliente.dic[cliente] for cliente in dic if dic[cliente][1]>25}

#dic = {"Pepe", {"Sur": "Boca", "Norte"}}

regiones = ["Norte", "Sur", ]

coso = input("Dame la región")
#lista[listaZonas.index(coso)]