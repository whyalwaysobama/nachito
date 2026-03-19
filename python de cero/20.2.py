pedidos_sandwiches = ["pastron", "jamon", "pastron", "queso", "pastron"]

print("No hay mas pastron")

while "pastron" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastron")

sandwiches_terminados = []

while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop()
    print(f"Prepare tu sándwich de {sandwich}")
    sandwiches_terminados.append(sandwich)

print("\nSandwiches terminados:")
print(sandwiches_terminados)