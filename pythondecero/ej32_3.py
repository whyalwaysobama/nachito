from pathlib import Path

ruta = Path("C:\\Users\\admin\\Documents\\GitHub\\nachito\\pythondecero\\learning_python.txt")
contenido = ruta.read_text()

lineas = contenido.splitlines()
for linea in lineas:
    print(linea.replace('Python', 'C'))
