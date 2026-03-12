import random

personas = ["maduro", "trump", "binladen"]

def main():
    persinvs()
    perchau()
    mgrande()
    solodos()
    print(personas)
def persinvs():
    for i in personas:
        print(f"hola {i} veni a la joda")

def perchau():
    perno = random.choice (personas)
    print(f"{perno} no puede venir")
    personas.remove(perno)
    personas.append("omaralgoandamal")
     
def mgrande():
    print(f"Hay una mesa mas grande vienen mas")
    personas.append("mrbean")
    personas.append("totote")
    personas.append("etesech")
    persinvs()

def solodos():
    print("solo dos personas pueden venir")
    while len(personas) > 2:
        perno = random.choice (personas)
        print(f"{perno} no puede venir")
        personas.remove(perno)
    for i in personas:
        print(f"{i} si puede venir")



main()