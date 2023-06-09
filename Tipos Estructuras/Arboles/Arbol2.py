class Nodo:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None

    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.derecho==None:
                raiz.derecho=nodo
            else:
                 raiz.derecho.agregarnodos(nodo)
        elif raiz.dato>nodo.dato:
            if raiz.izquierdo==None:
                raiz.izquierdo=nodo
            else:
                raiz.izquierdo.agregarnodos(nodo)

class arbolBinarioDeBusqueda():
    def insertar(self,valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_ordenado(valor,self.raiz)
    
    def insertar_ordenado(self,valor,nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.insertar_ordenado(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.insertar_ordenado(valor, nodo_actual.derecha)
    
    def buscar(self, valor):
        return self.buscar_recursivo(valor, self.raiz)
    
    def buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        
        if valor < nodo_actual.valor:
            return self.buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self.buscar_recursivo(valor, nodo_actual.derecha)
    
    def preorden(self):
        self.preorden_recursivo(self.raiz)
    
    def preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end="")
            #Primero buscamos siempre a la izquierda
            self.preorden_recursivo(nodo_actual.izquierda)
            #Luego de ir todo a la izquierda, vamos a la derecha
            self.preorden_recursivo(nodo_actual.derecha)

    def postorden(self):
        self.postorden_recusivo(self.raiz)
    
    def postorden_recusivo(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden_recusivo(nodo_actual.izquierda)
            self.postorden_recusivo(nodo_actual.derecha)
            print(nodo_actual.valor, end=" ")
    
    def guardar_estructura(self, nombre_archivo):
        #guarda el árbol en un archivo de texto
        with open(nombre_archivo, "w") as archivo:
            self.guardar_estructura_recursivo(self.raiz, archivo)
    
    def guardar_estructura_recursivo(self, nodo, archivo):
        #Método auxiliar para guardar la estructura el árbol en un archivo
        if nodo is None:
            return
        
        #Guardar la información del nodo en el archivo
        archivo.write(f'{nodo.valor}\n')

        #Llamada recursiva a los nodos izquierdo y derecho
        self.guardar_estructura_recursivo(nodo.izquierda, archivo)
        self.guardar_estructura_recursivo(nodo.derecho, archivo)





