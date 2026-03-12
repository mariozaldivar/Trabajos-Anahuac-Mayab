from Persona import Persona
from Medico import Medico
from Paciente import Paciente
from PacienteExterno import PacienteExterno
from PacienteHospitalizado import PacienteHospitalizado
running = True
print("Bienvenido al registro de pacientes, ¿qué le gustaría hacer?")

while running:
    try: 
        choice = int(input("Elija una opción: \n1) Registrar un paciente externo \n2) Registrar un paciente hospitalizado\n 3) Registrar un médico\n4) Salir del programa\n"))
        match choice:
            case 1: 
                nombre = input("Introduzca el nombre del paciente externo: ")
                apellido = input("Apellido: ")
                genero = input("Género: ")
                edad = int(input("Edad: "))
                altura = float(input("Altura en m: "))
                peso = float(input("Peso en kg: "))
                numCons = int(input("Número de consultorio: "))
                horario = int(input("Horario: "))
                fecha = input("Fecha: ")
                paciente_externo = PacienteExterno(nombre, apellido, genero, edad, altura, peso, numCons, horario, fecha)
                paciente_externo.printPaciente()
                paciente_externo.examenFisico()
                paciente_externo.imc()

            case 2: 
                nombre = input("Introduzca el nombre del paciente hospitalizado: ")
                apellido = input("Apellido: ")
                genero = input("Género: ")
                edad = int(input("Edad: "))
                altura = float(input("Altura en m: "))
                peso = float(input("Peso en kg: "))
                habitacion = int(input("Número de habitación: "))
                tipoCirugia = input("Tipo de cirugía: ")
                paciente_hospitalizado = PacienteHospitalizado(nombre, apellido, genero, edad, altura, peso, habitacion, tipoCirugia)
                paciente_hospitalizado.printPaciente()
                paciente_hospitalizado.indicaciones()
                paciente_hospitalizado.imc()


            case 3: 
                nombre = input("Introduzca el nombre del paciente hospitalizado: ")
                apellido = input("Apellido: ")
                genero = input("Género: ")
                edad = int(input("Edad: "))
                especialidad = input("Especialidad del médico: ")
                cedula_profesional = int(input("Cedula profesional del doctor: "))
                medico = Medico(nombre, apellido, genero, edad, especialidad, cedula_profesional)
                medico.printPersona()

            case 4:
                print("Saliendo del programa...")
                running = False

    except ValueError:
        print("Su elección no fue válida, introduzca un nuevo número")