from Paciente import Paciente
class PacienteExterno(Paciente):
    def __init__(self, nombre="John", apellido="Doe", genero="Masculino", edad="20", altura=1.70, peso=70.0, numCons=1, horario=10, fecha="1 de enero de 2026"):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self.__noConsultorio = numCons
        self.__horario = horario
        self.__fecha = fecha

    def examenFisico(self):
        print("Se programará un examen físico para el paciente...")

    def printPacienteExterno(self):
        super().printPaciente()
        print(f"""El número de consultorio del paciente externo es: {self.__numCons}
              El horario del paciente es: {self.__horario}
              La fecha es: {self.__fecha}""")



