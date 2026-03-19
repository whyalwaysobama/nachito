respuestas = {}

while True:
    nombre = input("Tu nombre: ")
    lugar = input("¿A dónde te gustaría viajar? ")

    respuestas[nombre] = lugar

    repetir = input("¿Otra persona? (si/no): ")
    if repetir.lower() == "no":
        break

print("\nResultados:")
for nombre, lugar in respuestas.items():
    print(f"{nombre} quiere ir a {lugar}")