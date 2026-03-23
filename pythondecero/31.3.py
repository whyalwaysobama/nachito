from random import choice
 
mi_boleto = [3, 7, 'b', 'e']
intentos = 0
 
resultado_igual = False
while not resultado_igual:
    boleto_sacado = []
    while len(boleto_sacado) < 4:
        elemento = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e'])
        if elemento not in boleto_sacado:
            boleto_sacado.append(elemento)
    intentos += 1
 
    if set(boleto_sacado) == set(mi_boleto):
        resultado_igual = True
 
print(f"\nGané después de {intentos} intentos.")