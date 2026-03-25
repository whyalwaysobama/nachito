def ciudad_pais(ciudad, pais, poblacion=None):
    if poblacion:
        return f"{ciudad.title()}, {pais.title()} - poblacion {poblacion}"
    return f"{ciudad.title()}, {pais.title()}"
