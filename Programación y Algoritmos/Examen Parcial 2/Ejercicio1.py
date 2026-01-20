# Mario Andrés Zaldívar de la Cruz
# ID: 00586553

def MemoriaRequerida(a:int, b:int):
    requerida = a*4.4 + b*7.3

    print(f"Se requerirán {requerida}kb de memoria")

    return requerida

def PuedeUsarLibreria(a, b, mem): 
        print(f"\nSe están utilizando {a+b} componentes\n")
        if (a+b) >= 9:
            print("Si se puede utilizar la librería")
            print(f"El ahorro sería de {mem*.25}kb")
            print(f"El uso de memoria total sería de {mem*.75}kb \n")
        else: 
            print("La librería para el ahorro de memoria no está disponible\n")
            
while True:

    while True:
        try:
            tipoA = int(input("Introduzca la cantidad de componentes tipo A (de conectividad) que se utilizarán: "))
            tipoB = int(input("Introduzca la cantidad de componentes tipo B (de procesamiento gráfico) que se utilizarán: "))

            break

        except ValueError:
            print("Esa no es una cantidad válida\n")

    
    print("")
    memoria = MemoriaRequerida(tipoA, tipoB)
    PuedeUsarLibreria(tipoA, tipoB, memoria)
    print("\n")

    siono = input("¿Desea continuar con el programa? Escriba si para continuar, no para terminar: ")
    print(siono.lower())
    while siono.lower() not in ("si", "no"):
        print("Esa no es una opción válida, introduzca su opción nuevamente ")
        siono = input("¿Desea continuar con el programa? Escriba si para continuar, no para terminar: ")
    if (siono == "no"):
        break
    