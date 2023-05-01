from array import array

vector = array("d", [1.2,3.5,6.9,7]) # este es con datos tipo double float
print(vector)

lista = [1, 4, 15, -6, -7]
vectorInt = array("i", lista)
print(vectorInt)

# Para recorrer
for dato in vectorInt:
    print(dato, end = "\t")

# Mostrar los elementos del vector de decimales desde la posición 1 a la 3
print(vector[1:3])

# modificar elementos del vector en un rango
vector[0:3] = array("d", [2.5,6.4,3.1])

# agregar elementos al final del array
vectorInt.extend([34, 21, 19])

# concatenar 2 arrays en uno
vector1 = array("i", [1,2,3,4,5])
vector2 = array("i", [6,7,8,9])
numeros = array("i")
numeros = vector1 + vector2
print(numeros)

# convertir un vector en una lista
lista = numeros.tolist()
print(lista)