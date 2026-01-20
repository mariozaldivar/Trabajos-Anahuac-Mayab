def CalcularIMC(peso: float, estatura: float) -> float:
    return peso/(estatura*estatura)

def EstadoDeSalud(imc: float) -> float:
    if imc < 18:
        print("Peso bajo. Necesario valorar signos de desnutrición")
    elif imc >= 18 and imc < 25:
        print("Peso normal")
    elif imc >= 25 and imc < 27:
        print("Sobrepeso")
    elif imc >= 27 and imc < 30: 
        print("Obesidad grado I. Riesgo relativo alto para desarrollar enfermedades cardiovasculares")
    elif imc >= 30 and imc < 40: 
        print("Obesidad grado II. Riesgo relativo muy alto para el desarrollo de enfermedades cardiovasculares")
    elif imc >= 40: 
        print("Obesidad grado III Extrema o Mórbida. Riesgo relativo extremadamente alto para el desarrollo de enfermedades cardiovasculares.")

    
peso = float(input("Introduzca el peso de la persona cuyo IMC quiere calcular en kg:  "))
estatura = float(input("Introduzca la estatura de la persona cuyo IMC desea calcular en metros:  "))
imc = CalcularIMC(peso, estatura)

print("El IMC de esta persona es de " + str(imc))
EstadoDeSalud(imc)