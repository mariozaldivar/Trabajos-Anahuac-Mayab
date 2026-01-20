import math


def CalcularPerimetro(radio: float) -> float:
    perimetro = (radio*2) * math.pi


    return perimetro


def CalcularArea(radio: float ) -> float:
    area = (radio*radio)*math.pi

    return area


while True: 
    try:
        radio = float(input("Introduzca el radio del círculo del cuál quiera realizar los cálculos:  "))
        break
    except ValueError: 
        print("Ese número no es válido, introduzca uno nuevo ")
print("El área del círculo de radio " + str(radio) + " es de: " + str(CalcularArea(radio)))
print("El perímetro del círculo de radio " + str(radio) + "es de: " + str(CalcularPerimetro(radio)))


