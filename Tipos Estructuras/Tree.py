"""
Todos  elementos almacenados son del mismo tipo. Cada nodo puede tener máximo 2 hijos. 
Implementación con memoria dinámica. Todo árbol tiene una raíz y es el padre de Hoja 1 y Hoja 2.  

Si todavía no ingresé nada, no tengo ningún nodo. Está señalando a None.

Si la información a ingresar es mayor que el valor guardado en el nodo padre, 
se ingresa el valor en la hoja de la derecha. Caso contrario, a izquierda.
Ingresado > Padre = Derecha 
Ingresado > Padre = Izquierda

Cada hijo implica un nuevo nivel, altura, o profundidad.

Operaciones:
    -Agregar Nodo
    -Eliminar Nodo
    -Recorridos.
        -Preorden(raíz, izquierdo, derecho):
            El árbol no debe estar vacío
            El recorrido utiliza las recursivas:
                Visite raíz
                Atraviese:
                    sub-árbol izquierdo
                    sub-árbol derecho
        -Postorden:
            Idem con recursivas:
                Atraviese el sub-árbol izquierdo
                Visite raiz
                Atraviese el sub-árbol derecho
        -Inorden:
            Idem con recursivas:
                Atraviese el sub-árbol izquierdo
                Visite raiz
                Atraviese el sub-árbol derecho

Ejemplo 0:
Preorden (R,I,D): F-B-A-D-C-E-G-I-H
Inorden (I,R,D): A-B-C-D-E-F-G-H-I
Postorden (I,D,R): A-C-E-D-B-H-I-G-F
"""
"""
class Nodo (self,valor):
	def __init__(self,valor):
		self.valor=valor
		self.Nodo_derecha=None
		self.Nodo_izquierda=None

public class Arbol :
	def __init__(self,nodo=None):
		Nodo raiz;

class Arbol ():
	def __init__(self,valor):
		self.valor=valor
		self.Nodo_derecha=None
		self.Nodo_izquierda=None
"""
