from Persona import Persona

class Medico(Persona):
    def __init__(self, nombre="John", apellido="Doe", genero="Masculino", edad=0, especialidad="Sin especialidad", cedula="1000000"):
        super().__init__
        self.especialidad = especialidad
        self.cedula_profesional = cedula

    def printMedico(self):
        print(f"""La especialidad del médico es: {self.especialidad}, y su cédula profesional es: {self.cedula_profesional}""")
        super().printPersona()