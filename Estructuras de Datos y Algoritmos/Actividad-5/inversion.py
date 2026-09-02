def calcularInversion(anos: int, dinero: float, interes: float) -> float:
    total = dinero
    if anos != 0:
        total = calcularInversion(anos - 1, dinero, interes)
        return total + (total * interes)
    return total


try:
    dinero = float(input("Introduce la cantidad de dinero que invertirás: $"))
    anos = int(input("Introduce la cantidad de años que lo invertirás: "))
    interes = float(input("Introduce el porcentaje de interes que tiene: ")) / 100
    print("$" + str(calcularInversion(anos, dinero, interes)))
except ValueError:
    print("El valor que introdujiste no es válido")
    exit()
