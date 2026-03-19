class admin:
    def __init__(self, nombre, apellido, edad, privilegios):
        self.nombre = nombre
        self.apellido = apellido
        self.privilegios = ["puede agregar post", "puede eliminar post", "puede banear usuarios"]

    def mostrar_privilegios(self):
        print(f"Privilegios de {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")
            
admin1 = admin("Dante", "Zurlo", 17, ["puede agregar post", "puede eliminar post", "puede banear usuarios"])
admin1.mostrar_privilegios()