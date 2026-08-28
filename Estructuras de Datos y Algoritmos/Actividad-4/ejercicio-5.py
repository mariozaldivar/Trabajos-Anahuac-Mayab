seen = set()
count = 0
filename = input("Introduce el nombre del archivo: ")

with open(filename, "r", encoding="utf-8") as file:
    texto = []
    for line in file:
        palabras = line.split(" ")
        if palabras[0] == "From: ":
            seen.add(palabras[2])
            count += 1
        else:
            pass

for user in seen:
    print(user)
