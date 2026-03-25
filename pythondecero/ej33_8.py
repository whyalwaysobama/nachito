from pathlib import Path
import json

ruta = Path('numero_favorito.json')

if ruta.exists():
    contenido = ruta.read_text()
    numero = json.loads(contenido)
    print(f"¡Sé cuál es tu número favorito! Es {numero}.")
else:
    numero = input("¿Cuál es tu número favorito? ")
    contenido = json.dumps(numero)
    ruta.write_text(contenido)
    print(f"Guardé tu número favorito: {numero}")
