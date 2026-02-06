from empleado import Empleado
empl_void = Empleado()
empl_void.Imprimir()
empl_void.calcularSalario()

empl = Empleado("Donald Trump", 2025, 200000)


while True: 
    try: 

        nombre = input("Introduzca el nombre del empleado: ")
        anio = int(input("Introduzca el anio de contratacion del empleado: "))
        salario = float(input("Introduzca el salario del empleado: "))
        break
    except ValueError:
        print("Introduzca un valor adecuado.")

empl_manual = Empleado(nombre, anio, salario)



