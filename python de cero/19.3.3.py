seguir = "si"

while seguir == "si":
    ingrediente = input("Ingrediente: ")

    if ingrediente == "salir":
        seguir = "no"
    else:
        print(f"Agregando {ingrediente}")