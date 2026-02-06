
class Empleado():
    def __init__(self, nombre="NULL", anioContratacion=0, salario=0.0):
        self.__nombre = nombre
        self.__anioContratacion = anioContratacion
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value


    @property
    def anioContratacion(self):
        return self.__anioContratacion
    
    @anioContratacion.setter
    def anioContratacion(self, value):
        self.__anioContratacion = value


    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def nombre(self, value):
        self.__salario = value


    def Imprimir(self):
        print(f"El nombre del empleado es: {self.__nombre}\nSe le contrato en el anio {self.__anioContratacion}\nSu salario mensual es de {self.__salario}")
        
    def calcularSalario(self):
        print(f"Dado que el salario mensual es de: {self.__salario}, su salario anual seria de {self.__salario*12}")
        return self.__salario*12