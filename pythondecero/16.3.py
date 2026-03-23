lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}

encuestapersonas = ['Juan', 'Sara', 'Eduardo', 'Jeffrey', 'Carlos']

for persona in encuestapersonas:
    if persona in lenguajes_favoritos:
        print(f"{persona}, gracias por participar en la encuesta. Tu lenguaje favorito es {lenguajes_favoritos[persona].title()}.")
    else:
        print(f"{persona}, ¿cuál es tu lenguaje de programación favorito?")

