from pathlib import Path
import json


def obtener_usuario_guardado(ruta):
    if ruta.exists():
        contenido = ruta.read_text()
        return json.loads(contenido)
    return None


def obtener_nuevo_usuario(ruta):
    nombre = input("¿Cuál es tu nombre? ")
    contenido = json.dumps(nombre)
    ruta.write_text(contenido)
    return nombre


def saludar_usuario():
    ruta = Path('username.json')
    nombre = obtener_usuario_guardado(ruta)
    if nombre:
        respuesta = input(f"¿Sos {nombre}? (si/no) ")
        if respuesta == 'si':
            print(f"Bienvenido de vuelta, {nombre}.")
        else:
            nombre = obtener_nuevo_usuario(ruta)
            print(f"Te voy a recordar, {nombre}.")
    else:
        nombre = obtener_nuevo_usuario(ruta)
        print(f"Te voy a recordar, {nombre}.")


saludar_usuario()
