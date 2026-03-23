edad = ""

while edad != "salir":
    edad = input("Ingresá tu edad (o salir): ")

    if edad != "salir":
        edad_num = int(edad)

        if edad_num < 3:
            print("Entrada gratis")
        elif edad_num <= 12:
            print("La entrada cuesta $10")
        else:
            print("La entrada cuesta $15")