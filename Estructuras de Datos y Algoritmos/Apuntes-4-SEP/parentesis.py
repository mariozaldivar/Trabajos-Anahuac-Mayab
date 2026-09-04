operacion = input(
    "Introduce una operación matemática, validaremos que tu uso de paréntesis sea adecuado: "
)

stack = []
relaciones = {"]": "[", "}": "{", ")": "("}
for letra in operacion:
    if letra == "{" or letra == "[" or letra == "(":
        stack.append(letra)
    elif letra in relaciones:
        if len(stack) == 0 or relaciones[letra] != stack[-1]:
            print("La operación no es válida")
            exit()
        else:
            stack.pop()

if len(stack) != 0:
    print("La operación no es válida")
    exit()

print("La operación es válida")
