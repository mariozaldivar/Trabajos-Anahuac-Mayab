

def main():
    print("Introduce la ocupación de los asientos representando los asientos ocupados como 1, y los desocupados como 0, con este formato: 1101110110")
    asientos = input()
    count = 0
    for asiento in asientos:
        try:
            asiento = int(asiento)
            if asiento != 0 and asiento != 1:
                print("No diste los asientos ocupados en el formato indicado")
            elif asiento == 1:
                count += 1
            elif asiento == 0:
                print("El asiento más próximo es el asiento número: ", (count + 1))
                exit()
        except ValueError:
            print("No diste los asientos ocupados en el formato indicado")


if __name__ == "__main__":
    main()
