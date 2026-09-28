class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def recorrido_in_order(self, nodo, resultado=None):
        if resultado is None:
            resultado = []
        if nodo is not None:
            self.recorrido_in_order(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self.recorrido_in_order(nodo.derecho, resultado)
        return resultado


if __name__ == "__main__":
    arbol = Arbol(1)

    arbol.raiz.izquierdo = Nodo(2)
    arbol.raiz.derecho = Nodo(3)

    arbol.raiz.izquierdo.izquierdo = Nodo(4)

    print("Recorrido In-Order del árbol:", arbol.recorrido_in_order(arbol.raiz))
