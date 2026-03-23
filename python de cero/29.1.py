class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir_restaurante(self):
        print(f"{self.nombre} - {self.tipo}")


class PuestoDeHelados(Restaurante):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.sabores = ["chocolate", "vainilla", "frutilla"]

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")


puesto = PuestoDeHelados("Helados Pepe", "Heladería")

puesto.describir_restaurante()
puesto.mostrar_sabores()