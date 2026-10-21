import os

ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temperaturas.txt")
numeros = []
fechas = []
try:
    with open(ruta, encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "" or linea.startswith("fecha"):
                continue
            fecha, temperatura = linea.split(",")
            fechas.append(fecha)
            numeros.append(float(temperatura))
except ValueError:
    print("El archivo contiene una temperatura que no es un número")


print("La lista como está en el archivo es:")
for i in range(len(numeros)):
    print(f"{fechas[i]}: {numeros[i]}")

sorted = False
# Ordenar ascendente
print("Orden ascendente: ")
while not sorted:
    sorted = True
    for i in range(len(numeros)):
        if i < len(numeros) - 1:
            if numeros[i] > numeros[i + 1]:
                buffer = numeros[i]
                numeros[i] = numeros[i + 1]
                numeros[i + 1] = buffer
                # Mover la fecha junto con su temperatura
                buffer = fechas[i]
                fechas[i] = fechas[i + 1]
                fechas[i + 1] = buffer
                sorted = False

for i in range(len(numeros)):
    print(f"{numeros[i]} - {fechas[i]}")

print("Orden descendente:")
descendente = numeros[::-1]
fechas_descendente = fechas[::-1]
for i in range(len(descendente)):
    print(f"{descendente[i]} - {fechas_descendente[i]}")
