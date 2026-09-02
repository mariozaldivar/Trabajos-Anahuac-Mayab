def obtenerSumaCuadrados(numero):
    obtenerSumaCuadrados.calls += 1
    suma = 0
    count = 0
    if numero != 1:
        suma = obtenerSumaCuadrados(numero - 1)
        suma += numero * numero
        return suma
    else:
        suma += 1
        return suma


try:
    print(
        "Calcula la sumatoria de los primeros n numeros al cuadrado. Escribe el valor de n: "
    )
    obtenerSumaCuadrados.calls = 0
    numero = int(input())
    resultado = obtenerSumaCuadrados(numero)
    print(f"Resultado: {resultado}")
    print(f"Cantidad de llamadas: {obtenerSumaCuadrados.calls}")
except ValueError:
    print("Ese número no puede ser convertido a un integer")
