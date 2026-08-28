seen = set()

filename = input("Introduce el nombre del archivo: ")

with open(filename, "r", encoding="utf-8") as file:
    texto = []
    for line in file:
        palabras = line.split(" ")
        for palabra in palabras:
            if palabra not in seen:
                palabra = palabra.replace("\n", "")
                texto.append(palabra)
                seen.add(palabra)
            else:
                pass

texto.sort()
print(texto)
