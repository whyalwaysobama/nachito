from pathlib import Path

nombre = input("¿Cuál es tu nombre? ")
ruta = Path('C:\\Users\\admin\\Documents\\GitHub\\nachito\\pythondecero\\guest.txt')
ruta.write_text(nombre)
print(f"Guardé tu nombre: {nombre}")
