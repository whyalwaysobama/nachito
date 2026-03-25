seguir = True

while seguir:
    num1 = input("\nIngresá el primer número (o 'salir' para terminar): ")
    if num1 == 'salir':
        seguir = False
    else:
        num2 = input("Ingresá el segundo número: ")
        if num2 == 'salir':
            seguir = False
        else:
            try:
                resultado = int(num1) + int(num2)
            except ValueError:
                print("Por favor ingresá solo números.")
            else:
                print(f"La suma es: {resultado}")
