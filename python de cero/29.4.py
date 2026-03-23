class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_nombre(self):
        return f"{self.año} {self.marca} {self.modelo}"


class Bateria:
    def __init__(self, capacidad=40):
        self.capacidad = capacidad

    def describir_bateria(self):
        print(f"Batería de {self.capacidad} kWh")

    def obtener_autonomia(self):
        if self.capacidad == 40:
            print("Autonomía: 150 km")
        else:
            print("Autonomía: 225 km")

    def actualizar_bateria(self):
        if self.capacidad < 65:
            self.capacidad = 65


class AutoElectrico(Auto):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()


auto = AutoElectrico("Tesla", "Model 3", 2024)

print(auto.obtener_nombre())

auto.bateria.obtener_autonomia()

auto.bateria.actualizar_bateria()

auto.bateria.obtener_autonomia()