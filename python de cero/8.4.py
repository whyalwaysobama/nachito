import random

personas = ["maduro", "trump", "binladen"]

def main():
    persinvs()
    perchau()

def persinvs():
    for i in personas:
        print(f"hola {i} veni a la joda")

def perchau():
    perno = random.choice (personas)
    print(f"{perno} no puede venir")
    personas.remove(perno)
    
     


main()