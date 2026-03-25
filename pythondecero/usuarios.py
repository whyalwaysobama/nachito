class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def describir_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre}!")


class Privilegios:
    def __init__(self):
        self.privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"  - {privilegio}")


class Administrador(Usuario):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = Privilegios()
