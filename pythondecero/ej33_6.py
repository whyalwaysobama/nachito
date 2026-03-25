from pathlib import Path

for nombre_archivo in ['pythondecero/gatos.txt', 'pythondecero/perros.txt']:
    ruta = Path(nombre_archivo)
    try:
        contenido = ruta.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contenido)
