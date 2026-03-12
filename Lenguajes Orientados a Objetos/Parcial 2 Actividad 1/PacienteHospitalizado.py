from Paciente import Paciente
class PacienteHospitalizado(Paciente):
    def __init__(self, nombre="John", apellido="Doe", genero="Masculino", edad="20", altura=1.70, peso=70.0, numCons=1, horario=10, fecha="1 de enero de 2026", habitacion=1, tipoCirugia="General"):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self.__habitacion = habitacion
        self.__tipoCirugia = tipoCirugia

    def indicaciones(self):
        print("Las indicaciones aún están por darse por el doctor")

    def printPacienteHospitalizado(self):
        super().printPaciente()
        print(f"""La habitación del paciente hospitalizado es la: {self.__habitacion}
        El tipo de cirugía para el paciente es: {self.__tipoCirugia}""")