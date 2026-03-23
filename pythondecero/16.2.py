rios = {"Nilo": "Egipto", 
        "Amazonas": "Brasil", 
        "Misisipi": "Estados Unidos"
        }

for rio, pais in rios.items():
    print(f"El río {rio} atraviesa {pais}.")

for rio in rios.keys():
    print(f"El río {rio} es uno de los ríos más importantes del mundo.")

for pais in rios.values():
    print(f"{pais} es un país atravesado por uno de los ríos más importantes del mundo.")