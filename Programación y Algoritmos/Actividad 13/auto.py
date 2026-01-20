print("Introduzca la cantidad de kilómetros recorridos")

try: 
    kilometros = float(input())
except (ValueError):
    print("Ese no es un número")

tarifa = 850

if kilometros > 200:
    tarifa = tarifa + ((kilometros - 200 )* 4.50)

print(f"Monto a pagar: ${tarifa:.2f}")
print(f"IVA: ${tarifa*.16:.2f}")
print(f"Monto total: ${tarifa*1.16:.2f}")