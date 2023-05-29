x = 100
y = 0
#Podemos usar el except
try:
    if(x<2000):
        print(x/y)
    else:
        print(x**y)
except ZeroDivisionError as e:
    print("Ha ocurrido un error. ", e)

#Podemos levantar el error
try:
    if(x<2000):
        if (y!=0):
            print(x/y)
        else:
            raise ValueError("División por cero")
    else:
        print("Else, bla bla bla")
except ValueError as e:
    print("Ha ocurrido un error. ", e)

#Podemos separar por distintos errores:
seguir = True
while (seguir==True):
    try:
        z = int(input("Ingrese un número distinto de CERO"))
        if(x<2000):
            if (z!=0):
                print(x/z)
                seguir = False
            else:
                raise ZeroDivisionError("División por cero")
        else:
            print("Else, bla bla bla")
    except ZeroDivisionError as e:
        print("Ha ocurrido un error: ", e)
    except ValueError:
        print("El dato introducido no corresponde al valor esperado")
print("Salimos del loop")

#Trabajar con archivos
from io import UnsupportedOperation

def existe(pathArchivo):
    try:
        archivo = open(pathArchivo,"r")
        return archivo
        archivo.write("Hola") #Está en modo escritura asi que se va a romper acá
    except FileNotFoundError:
        return None
    except UnsupportedOperation: #Lo tuvimos que importar a este coso
        print("El archivo está tratando de realizar una tarea no permitida")


pathArchivo = "C:/Users/agusa/Documents/GitHub/Apuntes-Estructura/Excepciones/errores.py"
manejarArchivo = existe(pathArchivo)
if manejarArchivo == None:
    print("El archivo no existe, salamin")
else:
    print("Archivo existe")
    for linea in manejarArchivo:
        print(linea)

#Uso del finally y el else
def dividir(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("División por cero...")
    else: #Si no se rompe, hace esto
        print(resultado)
    finally: #Lo hace siempre (sin importar que se rompa), después de todo lo anterior
        print("La ejecución de la función ha terminado")
dividir(1,0)
dividir(2,2)