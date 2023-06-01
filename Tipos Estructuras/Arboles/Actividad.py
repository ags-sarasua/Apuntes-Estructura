"""
Escriba un programa que lea un archivo CSV el cual contiene datos de personas( nombre, edad) 
y construya un árbol binario de búsqueda utilizando los nombres como clave.
"""
import csv
import Arbol2

with open('archivo.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # Omitir la primera fila (encabezados)
    for fila in lector_csv:
        nombre = fila[0]
        valor1 = fila[1]
        edad = fila[2]
        valor2 = fila[3]
        Arbol2.insertar(edad, valor1)        
        dicionario = {clave:valor for clave, valor in fila}
    print(dicionario)

#Le paso nombre y edad

"""
with open('archivo.csv', mode='r') as archivo:

    lector_csv = csv.reader(archivo)

    next(lector_csv)  # Omitir la primera fila

    for fila in lector_csv:

        clave = fila[0]

        valor = fila[1]

        dicionario = {clave:valor for clave, valor in fila}

    print(dicionario)
"""