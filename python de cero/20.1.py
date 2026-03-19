pedidos_sandwiches = ["jamon", "queso", "atun", "vegetal"]
sandwiches_terminados = []

while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop()
    print(f"Preparé tu sándwich de {sandwich}")
    sandwiches_terminados.append(sandwich)

print("\nSandwiches preparados:")
for s in sandwiches_terminados:
    print(s)