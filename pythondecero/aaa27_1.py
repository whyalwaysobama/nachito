class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre}, tipo: {self.tipo}")

    def abrir_restaurante(self):
        print("El restaurante está abierto")


restaurante = Restaurante("Lo de Pepe", "Parrilla")

print(restaurante.nombre)
print(restaurante.tipo)

restaurante.describir_restaurante()
restaurante.abrir_restaurante()

