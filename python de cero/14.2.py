personas = ["aba", "tole", "admin", "orse"]
for persona in personas:
    if persona == "admin":
        print("Hola admin, ¿quieres ver un informe de usuarios?")
    else:
        print(f"Hola {persona}, gracias por iniciar sesión.")

if personas == []:
    print("¡Necesitamos encontrar algunos usuarios!")