import numpy as np

# crear matrices
matriz = np.array([(1,8,2),(9,3,4)])
print(matriz)

# generar una matriz con datos aleatoria
matrizAleatoria = np.empty([2,2], dtype=int)
print(matrizAleatoria)

# matriz con ceros
matriz0 = np.zeros([2,3], dtype=int)
print(matriz0)

# pasar de un vector a una matriz
vector = np.arange(0,8)
print(vector)
matriz1 = np.arange(8).reshape(4,2)
print(matriz1)

#ordenar una matriz por columnas
matrizOrdenada = np.sort(matriz, axis=0) # si quiero ordenar por filas, sería axis 1
print("Matriz ordenada")
print(matrizOrdenada)
arrayOrdenado = np.sort(matriz, axis=None)
print(arrayOrdenado)