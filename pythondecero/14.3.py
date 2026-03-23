usuarios_actuales = ["aba", "tole", "jeffrey", "orse", "carlos"]

usuarios_nuevos = ["jeffrey", "tole", "totote", "david gogins", "pedro mickey mouse" ]

for usuario in usuarios_nuevos:
    if usuario in usuarios_actuales:
        print(f"El nombre de usuario '{usuario}' no está disponible. Por favor, elige otro.")
    else:
        print(f"El nombre de usuario '{usuario}' está disponible.")