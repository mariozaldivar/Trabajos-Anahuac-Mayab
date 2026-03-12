class Persona():

    def __init__(self, nombre="John", apellido="Doe", genero="Masculino", edad=0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__edad = edad

    def printPersona(self):
        print(f""" El nombre de la persona es: {self.__nombre},
              su apellido es: {self.__apellido}
              su edad es: {self.__edad},
              y su género es: {self.__genero},
""")
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, name:str):
        if name != "":
            self.__nombre = name
        else:
            print("El nombre no puede estar vacío")

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, lastname:str):
        if lastname != "":
            self.__apellido = lastname
        else:
            print("El apellido no puede estar vacío")


    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, gender:str):
        if gender != "":
            self.__genero = gender
        else:
            print("El genero no puede estar vacío")


    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, age:int):
        if age > 0:
            self.__edad = age
        else:
            print("La edad no puede ser menor a cero")



        






