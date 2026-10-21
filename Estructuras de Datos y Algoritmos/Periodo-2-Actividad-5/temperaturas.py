try:
    numeros = []
    numero = input(
        "Introduce la temperatura. Deja el campo vacío y presiona enter para hacer el cálculo: "
    )
    numeros.append(float(numero))
    while True:
        numero = input(
            "Introduce la temperatura. Deja el campo vacío y presiona enter para hacer el cálculo: "
        )
        if numero == "":
            break
        numeros.append(float(numero))
except ValueError:
    print("Eso no es un número")


print(f"La lista como la escribiste es: {numeros}")

sorted = False
# Ordenar ascendente
while not sorted:
    sorted = True
    for i in range(len(numeros)):
        if i < len(numeros) - 1:
            if numeros[i] < numeros[i + 1]:
                buffer = numeros[i]
                numeros[i] = numeros[i + 1]
                numeros[i + 1] = buffer
                sorted = False

print(numeros)
