from Persona import Persona

class Paciente(Persona):
    def __init__(self, nombre="John", apellido="Doe", genero="Masculino", edad="20", altura=1.70, peso=70.0):
        super().__init__(nombre, apellido, genero, edad)
        self.__altura = altura
        self.__peso = peso

    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, height:float):
        if height > 0:
            self.__altura = height
        else:
            print("La altura no puede ser menor a 0")


    @property
    def peso(self):
        return self.__peso  
    
    @peso.setter
    def peso(self, weight:float):
        if weight > 0:
            self.__peso = weight
        else:
            print("El peso no puede ser menor a 0kg")

    def printPaciente(self):
        print(f"""El peso del paciente es: {self.__peso},
              y su estatura es: {self.__altura}
""")
        super().printPersona()
        
    def imc(self):
        return (self.__peso / (self.__altura**2))


persona = Paciente()
persona.printPaciente()