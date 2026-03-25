num1 = input("Ingresá el primer número: ")
num2 = input("Ingresá el segundo número: ")

try:
    resultado = int(num1) + int(num2)
except ValueError:
    print("Por favor ingresá solo números.")
else:
    print(f"La suma es: {resultado}")
