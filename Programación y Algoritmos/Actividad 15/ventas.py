contador = 0
total = 0
venta = 1
destacadas = 0

while venta > 0:
    venta = float(input("Introduzca el monto de la venta (0 para terminar): "))
    if venta > 0:
        contador += 1
        total += venta
        if venta >= 1000:
            destacadas += 1

print(f"Ventas totales: {contador}")
print(f"Monto acumulado: ${total}", end="")
if total > 5000:
    print("  ¡Excelente jornada de ventas!", end="")
print("")
print(f"Promedio de la venta: ${total/contador}")
print(f"Ventas destacadas: {destacadas}")