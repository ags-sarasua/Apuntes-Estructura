def contains(lista, b):
    for i in lista:
        if(i==b):
            return True
    return False

lista = (1,2,3,4)
contains(lista, 4)

def busquedaBinaria(lista,x):
    izq = 0 #guarda el índice inicio del segmento
    der = len(lista)-1 #índice derecho del segmento

    #Un segmento es vacío cuando izq > der
    while izq <= der:
        medio = (izq+der)//2 #punto medio del segmento
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1

lista = [3,5,7,9,11,23,43,56]
dato = 111
esta = busquedaBinaria(lista, dato)
if esta == -1:
    print("El numero ",dato," no está en la lista")
else:
    print("El numero ",dato," está en la lista")

