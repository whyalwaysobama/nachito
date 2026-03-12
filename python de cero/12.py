pizzas_amigo = ["margarita", "muzza", "pepperoni"]
pizzas = ["margarita", "muzza", "pepperoni"]

pizzas_amigo.append("faina")

print(f"mis pizzas favoritas son:")
for i in pizzas:
    print(f"{i}")

print(f"las pizzas favoritas de mi amigo son:")
for i in pizzas_amigo:
    print(f"{i}")