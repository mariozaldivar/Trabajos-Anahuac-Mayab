class Usuario:

    def __init__(self, nombre:str, apellidos:str, edad:int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def IniciarSesion(self):
        print(f"El usuario {self.nombre} esta iniciando sesion")

    def CerrarSesion(self):
        print(f"El usuario {self.nombre} esta cerrando sesion")

    def HacerReporte(self):
        print("Reporte de Usuario")
        print(f"Su nombre completo es {self.nombre} {self.apellidos}.")
        print(f"Su edad es de {self.edad} años")




    
