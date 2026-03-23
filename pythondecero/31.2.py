from random import choice
 
posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
ganadores = []
 
while len(ganadores) < 4:
    elemento = choice(posibles)
    if elemento not in ganadores:
        ganadores.append(elemento)
 
print(f"\nEl boleto ganador tiene: {ganadores}")