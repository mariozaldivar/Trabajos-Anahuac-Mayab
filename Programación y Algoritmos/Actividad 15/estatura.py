print("Introduzca consecutivamente las estaturas de los 5 alumnos en centímetros")


total = 0
contador = 0
for i in range(5):
    estatura = 0
    while estatura < 110 or estatura > 220:
        estatura = int(input("Introduzca la estatura del alumno " + str(i + 1) + ": "))

    total += estatura
    if estatura > 170:
        contador += 1
    
print(f"El promedio de estatura es de {total/5}cm")
print(f"Hay {contador} alumnos más altos que 170")