from city_functions import ciudad_pais


def test_city_country():
    resultado = ciudad_pais('santiago', 'chile')
    assert resultado == 'Santiago, Chile'
    print(resultado)