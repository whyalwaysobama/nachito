from pathlib import Path

archivos = [Path('pythondecero/alice.txt'), Path('pythondecero/moby_dick.txt')]

for nombre in archivos:
    ruta = Path(nombre)
    try:
        contenido = ruta.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"No se encontró {nombre}.")
    else:
        cantidad = contenido.lower().count('the ')
        print(f"{nombre} tiene aproximadamente {cantidad} apariciones de 'the'.")
