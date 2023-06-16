from claseNodoArbol import *
class arbol:
    def __init__(self,nodo=None):
        self.root=nodo
       
    # agregar al arbol
    def agregarnodo(self,nodo):
        if self.root is None:
            self.root=nodo
        else:
            root=self.root
            #NodoArbol.agregarnodos(root,nodo)
            root.agregarnodos(nodo)
    
    def buscarNodo(self,nodo):
        if self.root is None:
            return("Este árbol está vacío")
        pass

   # Mostrar el arbol en preorden
    def preorder(nodo):
        if nodo:
            print(nodo.dato)
            arbol.preorder(nodo.izquierdo)
            arbol.preorder(nodo.derecho)
    
    # Mostrar el arbol en inorden
    def inorder(nodo):
        if(nodo):
            arbol.inorder(nodo.izquierdo)
            print(nodo.dato)
            arbol.inorder(nodo.derecho)
    
    # Mostrar en postorden
    def posorden(nodo):
        if nodo:
            arbol.posorden(nodo.izquierdo)
            arbol.posorden(nodo.derecho)
            print(nodo.dato)






