class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def describir_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre}!")
