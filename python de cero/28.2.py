class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_login = 0

    def incrementar_intentos(self):
        self.intentos_login += 1

    def reiniciar_intentos(self):
        self.intentos_login = 0


u = Usuario("Dante", "Zurlo")

u.incrementar_intentos()
u.incrementar_intentos()
u.incrementar_intentos()

print(u.intentos_login)

u.reiniciar_intentos()
print(u.intentos_login)