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

"""
if eleccion_metodo=='3':
    print('1)Nro vuelo  2)Aeropuerto salida  3)Aeropuerto llegada    4)Legajo del piloto   5)Precio')
    print('\n \t Comentario')
    print('Nro vuelo: 4 digitos numericos \n')
    input_principal=input("ingrese el Nro de vuelo del vuelo a actualizar:    ")
    input_principal=Clases.vuelo.check_sintaxis_nro_vuelo(input_principal)
    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
    nuevo_input=input("Ingrese el valor a actualizar:    ")

    if eleccion_actualizar in ['1','2','3','4','5']:
        if eleccion_actualizar=="1":
            nuevo_input=Clases.vuelo.check_sintaxis_nro_vuelo(nuevo_input)
            if arbol_vuelo.actualizar_le(input_principal,"nro_vuelo","nro_vuelo",nuevo_input) == False:
                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")
        if eleccion_actualizar=="2":
            if arbol_vuelo.actualizar_le(input_principal,"nro_vuelo","aeropuerto_salida",nuevo_input) == False:
                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

        if eleccion_actualizar=="3":
            if arbol_vuelo.actualizar_le(input_principal,"nro_vuelo","aeropuerto_llegada",nuevo_input) == False:
                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

        if eleccion_actualizar=="4":
            nuevo_input=Clases.vuelo.check_piloto(nuevo_input,lista_empleado) 
            if arbol_vuelo.actualizar_le(input_principal,"nro_vuelo","legajo_piloto",nuevo_input) == False:
                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

        if eleccion_actualizar=="5":
            nuevo_input=Clases.vuelo.check_precio_vuelo(nuevo_input)
            if arbol_vuelo.actualizar_le(input_principal,"nro_vuelo","precio",nuevo_input)  == False:
                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")                

    else:
        print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")                
"""

"""
        lista_empleado=json_a_normal(Clases.empleado,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\empleado.json')
        lista_avion=json_a_normal(Clases.avion,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\avion.json') 
        lista_persona=json_a_enlazada(Clases.persona,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\persona.json','fecha_de_nacimiento')
        arbol_vuelo=json_a_enlazada(Clases.vuelo,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\vuelo.json') 
        lista_viaje=json_a_enlazada(Clases.viaje,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\viaje.json','fecha','pasajeros',Clases.persona,'fecha_de_nacimiento')
        lista_reserva=json_a_enlazada(Clases.reserva,r'C:\Users\USER\Documents\GitHub\TP-2P\Jsons\reserva.json')
        print('')
"""