TAMANO = 10
tabla = [None] * TAMANO

print("Valores iniciales sugeridos: 25 18 42 38 13 27")
entrada = input(
    "Ingresa los números separados por espacio (Enter para usar los iniciales): "
).strip()
if entrada == "":
    entrada = "25 18 42 38 13 27"
valores = [int(n) for n in entrada.split()]

# Mostrar el cálculo de la función hash
print("\nCálculo de h(x) = x mod 10")
for x in valores:
    print(f"h({x}) = {x} mod 10 = {x % TAMANO}")

# Insertar en la tabla
print("\nInsertando valores:")
for x in valores:
    pos = x % TAMANO
    intentos = 0
    while tabla[pos] is not None and intentos < TAMANO:
        pos = (pos + 1) % TAMANO
        intentos += 1
    if intentos == TAMANO:
        print(f"  Tabla llena, no se pudo insertar {x}")
    elif intentos > 0:
        print(
            f"  Colisión: {x} debía ir en {x % TAMANO} (ocupada por {tabla[x % TAMANO]}), se guarda en {pos}"
        )
        tabla[pos] = x
    else:
        print(f"  {x} -> posición {pos}")
        tabla[pos] = x

print("\nPosición | Valor")
print("---------+------")
for i in range(TAMANO):
    print(f"{i:^8} | {tabla[i] if tabla[i] is not None else '-'}")

while True:
    dato = input("\nNúmero a buscar (Enter para salir): ").strip()
    if dato == "":
        break
    x = int(dato)
    pos = x % TAMANO
    intentos = 0
    encontrado = False
    while tabla[pos] is not None and intentos < TAMANO:
        if tabla[pos] == x:
            encontrado = True
            break
        pos = (pos + 1) % TAMANO
        intentos += 1
    if encontrado:
        print(f"{x} encontrado en la posición {pos} (h({x}) = {x % TAMANO})")
    else:
        print(f"{x} no está en la tabla")
