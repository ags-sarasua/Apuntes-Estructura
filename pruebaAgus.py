def capicua(lista, i = 0, cont = 0):
    if(i!=len(lista)):
        if str(lista[i]) == str(lista[i])[::-1]:
            return "La lista tiene un capicua"
        if cont == 0:
            a = capicua(lista, i+1)
    else:
        return "No hay"
    return a

print(capicua([12,34,54,44445,67,88888]))