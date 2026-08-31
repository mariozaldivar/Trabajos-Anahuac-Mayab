class Ingrediente:
    def __init__(self, value):
        self.ingredient = value
        self.next_ingredient = None


class Postre:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        if ingredientes is not None:
            primer_ingrediente = Ingrediente(ingredientes[0])
            self.primer_ingrediente = primer_ingrediente
            current_ingrediente = primer_ingrediente
            for ingrediente in ingredientes:
                if ingrediente != current_ingrediente.ingredient:
                    nuevo_ingrediente = Ingrediente(ingrediente)
                    current_ingrediente.next_ingredient = nuevo_ingrediente
                    current_ingrediente = nuevo_ingrediente

    def imprimir_ingredientes(self):
        current_ingrediente = self.primer_ingrediente
        while current_ingrediente is not None:
            print(current_ingrediente.ingredient)
            current_ingrediente = current_ingrediente.next_ingredient

    def eliminar_ingrediente_de_nombre(self, nombre):
        ptr1 = self.primer_ingrediente
        ptr2 = self.primer_ingrediente

        while ptr1 is not None:
            if ptr1.ingredient == nombre:
                if ptr1 is self.primer_ingrediente:
                    self.primer_ingrediente = ptr1.next_ingredient

                else:
                    ptr2.next_ingredient = ptr1.next_ingredient

                return
            ptr2 = ptr1
            ptr1 = ptr1.next_ingredient

    def agregar_ingrediente(self, nombre):
        nuevo_ingrediente = Ingrediente(nombre)
        if self.primer_ingrediente is None:
            self.primer_ingrediente = nuevo_ingrediente
            return
        current_ingrediente = self.primer_ingrediente
        while current_ingrediente.next_ingredient is not None:
            current_ingrediente = current_ingrediente.next_ingredient
        current_ingrediente.next_ingredient = nuevo_ingrediente


class Postres:
    def __init__(self, postres):
        self.postres = postres

    def imprimir_postre_de_nombre(self, nombre):
        for postre in self.postres:
            if postre.nombre == nombre:
                print(f"Nombre del postre {nombre}:")
                postre.imprimir_ingredientes()
                return
        print("No se encontró un postre con ese nombre")

    def eliminar_ingrediente_de_postre(self, nombre_postre, nombre_ingrediente):
        for postre in self.postres:
            if postre.nombre == nombre_postre:
                postre.eliminar_ingrediente_de_nombre(nombre_ingrediente)
                return
        print("No se encontró un postre con ese nombre")

    def agregar_ingrediente_a_postre(self, nombre_postre, nombre_ingrediente):
        for postre in self.postres:
            if postre.nombre == nombre_postre:
                postre.agregar_ingrediente(nombre_ingrediente)
                return
        print("No se encontró un postre con ese nombre")


postre1 = Postre(
    "Pay",
    ["Limon", "Queso", "Pan"],
)
postre2 = Postre("Pastel", ["Chocolate", "Pan"])
postres = Postres([postre1, postre2])
postres.imprimir_postre_de_nombre("Pay")
