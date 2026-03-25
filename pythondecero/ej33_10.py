from pathlib import Path
import json

ruta = Path('persona.json')

if ruta.exists():
    contenido = ruta.read_text()
    persona = json.loads(contenido)
    print(f"Recuerdo que sos {persona['nombre']}, tenés {persona['edad']} años y vivís en {persona['ciudad']}.")
else:
    nombre = input("¿Cuál es tu nombre? ")
    edad = input("¿Cuántos años tenés? ")
    ciudad = input("¿En qué ciudad vivís? ")
    persona = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
    contenido = json.dumps(persona)
    ruta.write_text(contenido)
    print(f"Te voy a recordar, {nombre}.")
