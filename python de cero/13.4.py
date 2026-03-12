import random

vida = list(range(1,101))

edad = random.choice(vida)

if edad < 2:
    print(f"es un bebe, tiene {edad} años")
elif edad < 4 and edad >= 2:
    print(f"es un nene/a chiquito/a, tiene {edad} años")
elif edad < 13 and edad >= 4:
    print(f"es un nene/a, tiene {edad} años")
elif edad < 20 and edad >= 13:
    print(f"es un adolescente, tiene {edad} años")
elif edad < 65 and edad >= 20:
    print(f"es un adulto/a, tiene {edad} años")
else:
    print(f"es un anciano/a, tiene {edad} años")