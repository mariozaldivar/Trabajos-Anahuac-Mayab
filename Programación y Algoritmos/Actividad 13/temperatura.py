fahrenheit = float(input("Introduzca la temperatura en grados Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

if celsius < 20:
    mensaje = "no calsificada"
    
elif celsius > 20 and celsius <= 25:
    mensaje = "ideal"

elif celsius > 25 and celsius <= 32:
    mensaje = "peligrosa"
elif celsius > 32:
    mensaje = "contraindicada"

print(f"La temperatura equivale a {celsius:.2f} grados Celsius, por lo que es {mensaje}")