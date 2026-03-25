from pathlib import Path

ruta = Path("C:\\Users\\admin\\Documents\\GitHub\\nachito\\pythondecero\\learning_python.txt")
contenido = ruta.read_text()

print("--- Leyendo todo el archivo ---")
print(contenido)

print("--- Leyendo línea por línea ---")
lineas = contenido.splitlines()
for linea in lineas:
    print(linea)
