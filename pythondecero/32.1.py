from pathlib import Path

ruta = Path("C:\\Users\\admin\\Documents\\GitHub\\nachito\\pythondecero\\pi.txt")
contenido = ruta.read_text()

cumple = input("Ingresá tu cumpleaños (ddmmaa): ")
if cumple in contenido:
    print("¡Tu cumpleaños aparece en los primeros un millón de dígitos de pi!")
else:
    print("Tu cumpleaños no aparece en los primeros un millón de dígitos de pi.")