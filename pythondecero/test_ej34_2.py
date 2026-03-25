from city_functions_v2 import ciudad_pais


def test_city_country():
    resultado = ciudad_pais('santiago', 'chile')
    assert resultado == 'Santiago, Chile'


def test_city_country_population():
    resultado = ciudad_pais('santiago', 'chile', poblacion=5000000)
    assert resultado == 'Santiago, Chile - poblacion 5000000'
