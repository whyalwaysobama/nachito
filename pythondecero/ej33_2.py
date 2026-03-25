from pathlib import Path

nombres = ""
seguir = True

while seguir:
    nombre = input("¿Cuál es tu nombre? (escribe 'salir' para terminar) ")
    if nombre == 'salir':
        seguir = False
    else:
        nombres += nombre + "\n"

ruta = Path('C:\\Users\\admin\\Documents\\GitHub\\nachito\\pythondecero\\guest_book.txt')
ruta.write_text(nombres)
print("Nombres guardados en guest_book.txt")
