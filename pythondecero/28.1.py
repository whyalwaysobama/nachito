class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.clientes_atendidos = 0

    def mostrar_clientes(self):
        print(f"Clientes atendidos: {self.clientes_atendidos}")

    def establecer_clientes(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes(self, cantidad):
        self.clientes_atendidos += cantidad


r = Restaurante("Lo de Pepe", "Parrilla")

r.mostrar_clientes()

r.establecer_clientes(10)
r.mostrar_clientes()

r.incrementar_clientes(5)
r.mostrar_clientes()