
class Node():
    __init__(self, value): 
        self.value = value
        self.next = None


class LinkedList(): 
    def __init__(self, primerNodo): 
        self.primerNodo = primerNodo
        self.nodoActual = primerNodo

    def imprimir(self): 
        self.nodoActual = self.primerNodo
        while (self.nodoActual.next != None):
            print(self.nodoActual.value)
            self.nodoActual = self.nodoActual.next

    def insertarFinal(self, nodoNuevo): 
        while (self.nodoActual.next != None): 
            self.nodoActual = self.nodoActual.next
        self.nodoActual.next = nodoNuevo
    def insertarPrincipio(self, nodoNuevo): 
        nodoNuevo.next = self.primerNodo
        self.primerNodo = nodoNuevo

primerNodo = LinkedList(5)


