class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def obtener_nombre(self):
        return f"{self.año} {self.marca} {self.modelo}"

    def mostrar_kilometraje(self):
        print(f"Kilometraje: {self.kilometraje} km")

    def actualizar_kilometraje(self, km):
        self.kilometraje = km

    def incrementar_kilometraje(self, km):
        self.kilometraje += km


mi_auto = Auto("Toyota", "Corolla", 2020)

print(mi_auto.obtener_nombre())

mi_auto.mostrar_kilometraje()

mi_auto.actualizar_kilometraje(100)
mi_auto.mostrar_kilometraje()

mi_auto.incrementar_kilometraje(50)
mi_auto.mostrar_kilometraje()