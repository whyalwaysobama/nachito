class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def describir_usuario(self):
        print(f"{self.nombre} {self.apellido}, edad {self.edad}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre}!")


u1 = Usuario("Dante", "Zurlo", 17)
u2 = Usuario("Fabian", "Perez", 20)

u1.describir_usuario()
u1.saludar_usuario()

u2.describir_usuario()
u2.saludar_usuario()