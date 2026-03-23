from random import randint
 
class Dado:
    """Representa un dado."""
    def __init__(self, lados=6):
        self.lados = lados
 
    def tirar(self):
        resultado = randint(1, self.lados)
        print(resultado)
 
 
dado_6 = Dado()
print("Dado de 6 caras:")
for i in range(10):
    dado_6.tirar()
 
dado_10 = Dado(10)
print("\nDado de 10 caras:")
for i in range(10):
    dado_10.tirar()
 
dado_20 = Dado(20)
print("\nDado de 20 caras:")
for i in range(10):
    dado_20.tirar()
 